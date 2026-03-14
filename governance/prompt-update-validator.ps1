# Prompt Update Validator and Auto-Commit Script (Windows PowerShell)
# This script validates prompt integrity and creates automatic commits for chat-prompt-en.md updates

param(
    [switch]$Force
)

$ErrorActionPreference = "Stop"

# Set project root (parent directory of governance folder)
$ProjectRoot = Split-Path $PSScriptRoot -Parent
$PromptFile = Join-Path $ProjectRoot "chat-prompt-en.md"
$ValidatorScript = Join-Path $PSScriptRoot "prompt-update-validator.py"
$ExpectedPrompts = 15

# Required sections
$RequiredSections = @(
    "Global Rules for Prompt Management",
    "Knowledge Base Foundation Prompts", 
    "Update Records",
    "Version History",
    "Directory Structure Summary",
    "Quick Reference"
)

function Write-Header {
    Write-Host "=" * 60 -ForegroundColor Cyan
    Write-Host "PROMPT UPDATE VALIDATOR AND AUTO-COMMIT" -ForegroundColor Cyan
    Write-Host "=" * 60 -ForegroundColor Cyan
}

function Test-PromptIntegrity {
    param([string]$Content)
    
    $Result = @{
        Valid = $true
        MissingPrompts = @()
        FoundPrompts = @()
        Issues = @()
    }
    
    # Check for all 15 prompts
    for ($i = 1; $i -le $ExpectedPrompts; $i++) {
        $Pattern = "^### Prompt $i\s*\("
        $Matches = [regex]::Matches($Content, $Pattern, [System.Text.RegularExpressions.RegexOptions]::Multiline)
        if ($Matches.Count -eq 0) {
            $Result.Valid = $false
            $Result.MissingPrompts += "Prompt $i"
        } else {
            $Result.FoundPrompts += "Prompt $i"
        }
    }
    
    # Check for required sections
    foreach ($Section in $RequiredSections) {
        if ($Content -notmatch [regex]::Escape($Section)) {
            $Result.Valid = $false
            $Result.Issues += "Missing required section: $Section"
        }
    }
    
    # Check for duplicate prompts
    $PromptPattern = "^### Prompt \d+\s*\("
    $Prompts = [regex]::Matches($Content, $PromptPattern, [System.Text.RegularExpressions.RegexOptions]::Multiline)
    if ($Prompts.Count -ne ($Prompts | Select-Object -Unique).Count) {
        $Result.Valid = $false
        $Result.Issues += "Duplicate prompts detected"
    }
    
    return $Result
}

function Test-UpdateRecordExists {
    param([string]$Content)
    
    $Today = Get-Date -Format "yyyy-MM-dd"
    return $Content -match "Update $Today"
}

function New-ValidationReport {
    param([hashtable]$ValidationResult, [bool]$UpdateRecordExists)
    
    $Report = @{
        Timestamp = (Get-Date).ToString("o")
        PromptFile = $PromptFile
        Validation = $ValidationResult
        UpdateRecordExists = $UpdateRecordExists
        TotalPromptsExpected = $ExpectedPrompts
        TotalPromptsFound = $ValidationResult.FoundPrompts.Count
        ReadyForCommit = $ValidationResult.Valid -and $UpdateRecordExists
    }
    
    return $Report
}

function Save-ValidationReport {
    param([hashtable]$Report)
    
    $GovernanceDir = Join-Path $ProjectRoot "governance"
    if (!(Test-Path $GovernanceDir)) {
        New-Item -ItemType Directory -Path $GovernanceDir -Force | Out-Null
    }
    
    $ReportFile = Join-Path $GovernanceDir ("prompt-validation-{0:yyyyMMdd-HHmmss}.json" -f (Get-Date))
    $Report | ConvertTo-Json -Depth 10 | Out-File -FilePath $ReportFile -Encoding UTF8
    
    return $ReportFile
}

function Invoke-GitCommit {
    param([string]$Message)
    
    try {
        # Check if git repository
        if (!(Test-Path (Join-Path $ProjectRoot ".git"))) {
            Write-Host "Not a git repository, skipping commit" -ForegroundColor Yellow
            return $false
        }
        
        # Change to project root directory
        $OriginalLocation = Get-Location
        Set-Location $ProjectRoot
        
        try {
            # Stage prompt file (relative path from project root)
            $RelativePromptFile = "chat-prompt-en.md"
            $StageResult = git add $RelativePromptFile 2>&1
            if ($LASTEXITCODE -ne 0) {
                throw "Failed to stage prompt file: $StageResult"
            }
            
            # Check if there are changes to commit (only for the prompt file)
            $StatusResult = git status --porcelain $RelativePromptFile 2>&1
            if ($StatusResult -eq $null -or $StatusResult.Count -eq 0 -or ($StatusResult -join "").Trim() -eq "") {
                Write-Host "✓ Nothing to commit (no changes)" -ForegroundColor Green
                return $true
            }
            
            # Create commit
            $CommitResult = git commit -m $Message 2>&1
            if ($LASTEXITCODE -ne 0) {
                throw "Failed to create commit: $CommitResult"
            }
            
            Write-Host "✓ Auto-commit created: $Message" -ForegroundColor Green
            return $true
        }
        finally {
            # Restore original location
            Set-Location $OriginalLocation
        }
        
    } catch {
        Write-Host "✗ Failed to create auto-commit: $_" -ForegroundColor Red
        return $false
    }
}

function Invoke-ValidationAndCommit {
    Write-Header
    
    # Check if prompt file exists
    if (!(Test-Path $PromptFile)) {
        Write-Host "❌ Prompt file not found: $PromptFile" -ForegroundColor Red
        return $false
    }
    
    # Read prompt file content
    $Content = Get-Content $PromptFile -Raw -Encoding UTF8
    
    # Run validation
    $ValidationResult = Test-PromptIntegrity -Content $Content
    $UpdateRecordExists = Test-UpdateRecordExists -Content $Content
    
    # Create report
    $Report = New-ValidationReport -ValidationResult $ValidationResult -UpdateRecordExists $UpdateRecordExists
    
    # Print validation results
    Write-Host "`nValidation Results:" -ForegroundColor Cyan
    Write-Host "  Total Prompts Expected: $($Report.TotalPromptsExpected)" -ForegroundColor White
    Write-Host "  Total Prompts Found: $($Report.TotalPromptsFound)" -ForegroundColor $(if ($Report.TotalPromptsFound -eq $ExpectedPrompts) { "Green" } else { "Red" })
    Write-Host "  Validation Status: $(if ($ValidationResult.Valid) { '✓ PASSED' } else { '✗ FAILED' })" -ForegroundColor $(if ($ValidationResult.Valid) { "Green" } else { "Red" })
    Write-Host "  Update Record: $(if ($UpdateRecordExists) { '✓ EXISTS' } else { '✗ MISSING' })" -ForegroundColor $(if ($UpdateRecordExists) { "Green" } else { "Yellow" })
    Write-Host "  Ready for Commit: $(if ($Report.ReadyForCommit) { '✓ YES' } else { '✗ NO' })" -ForegroundColor $(if ($Report.ReadyForCommit) { "Green" } else { "Red" })
    
    # Check for issues
    if (!$ValidationResult.Valid) {
        Write-Host "`n❌ Issues found:" -ForegroundColor Red
        foreach ($Issue in $ValidationResult.Issues) {
            Write-Host "  - $Issue" -ForegroundColor Red
        }
        if ($ValidationResult.MissingPrompts.Count -gt 0) {
            Write-Host "  - Missing prompts: $($ValidationResult.MissingPrompts -join ', ')" -ForegroundColor Red
        }
        
        # Save validation report even if failed
        Save-ValidationReport -Report $Report | Out-Null
        return $false
    }
    
    if (!$UpdateRecordExists) {
        Write-Host "`n⚠️  Warning: No update record found for today's changes" -ForegroundColor Yellow
        Write-Host "   Please add an update record in 'Update Records' section" -ForegroundColor Yellow
        
        # Save validation report
        $ReportFile = Save-ValidationReport -Report $Report
        Write-Host "`n📄 Validation report saved: $ReportFile" -ForegroundColor Cyan
        
        if (!$Force) {
            Write-Host "`n❌ Cannot proceed with auto-commit without update record" -ForegroundColor Red
            return $false
        }
    }
    
    # Save validation report
    $ReportFile = Save-ValidationReport -Report $Report
    Write-Host "`n📄 Validation report saved: $ReportFile" -ForegroundColor Cyan
    
    # Create auto-commit
    if ($Report.ReadyForCommit -or $Force) {
        $CommitMessage = "Update chat-prompt-en.md - $(Get-Date -Format 'yyyy-MM-dd')"
        $Success = Invoke-GitCommit -Message $CommitMessage
        
        if ($Success) {
            Write-Host "`n✅ Process completed successfully!" -ForegroundColor Green
            return $true
        } else {
            Write-Host "`n❌ Auto-commit failed" -ForegroundColor Red
            return $false
        }
    }
    
    return $false
}

# Main execution
try {
    $Success = Invoke-ValidationAndCommit
    exit $(if ($Success) { 0 } else { 1 })
} catch {
    Write-Host "❌ Error: $_" -ForegroundColor Red
    Write-Host $_.ScriptStackTrace -ForegroundColor Red
    exit 1
}
