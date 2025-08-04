Write-Host '=== Configuração de Navegadores (Usuário) ===' -ForegroundColor Green

# ===== CONFIGURAÇÕES =====
$HtmlBookmarksPath = 'C:\Users\Carlos\Desktop\teste.html'  # ALTERE AQUI
$StartupUrl1 = 'https://outlook.live.com'                     # ALTERE AQUI
$StartupUrl2 = 'https://www.oliveiraeantunes.com.br'                    # ALTERE AQUI

# ===== VERIFICAR SE É ADMINISTRADOR =====
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] 'Administrator')

if ($isAdmin) {
    Write-Host '✅ Executando como Administrador - Usando configurações globais' -ForegroundColor Green
    $chromePolicyPath = 'HKLM:\SOFTWARE\Policies\Google\Chrome'
    $edgePolicyPath = 'HKLM:\SOFTWARE\Policies\Microsoft\Edge'
} else {
    Write-Host '⚠️  Executando como usuário normal - Usando configurações locais' -ForegroundColor Yellow
    $chromePolicyPath = 'HKCU:\SOFTWARE\Policies\Google\Chrome'
    $edgePolicyPath = 'HKCU:\SOFTWARE\Policies\Microsoft\Edge'
}

# ===== VERIFICAR ARQUIVO DE FAVORITOS =====
if (!(Test-Path $HtmlBookmarksPath)) {
    Write-Host 'ATENÇÃO: Arquivo de favoritos não encontrado!' -ForegroundColor Red
    $newPath = Read-Host 'Digite o caminho do arquivo HTML (ou ENTER para pular)'
    if ($newPath -and (Test-Path $newPath)) {
        $HtmlBookmarksPath = $newPath
    } else {
        $HtmlBookmarksPath = $null
    }
}

# ===== INSTALAR CHROME (se necessário) =====
$chromeExe = "${env:ProgramFiles}\Google\Chrome\Application\chrome.exe"
$chromeExeUser = "${env:LOCALAPPDATA}\Google\Chrome\Application\chrome.exe"

# Verificar instalação do Chrome (global ou usuário)
if (!(Test-Path $chromeExe) -and !(Test-Path $chromeExeUser)) {
    Write-Host 'Chrome não encontrado. Baixando instalador para usuário...' -ForegroundColor Yellow
    
    try {
        $chromeUrl = 'https://dl.google.com/chrome/install/ChromeStandaloneSetup.exe'
        $installer = "$env:TEMP\chrome_user.exe"
        
        Invoke-WebRequest -Uri $chromeUrl -OutFile $installer -UseBasicParsing
        Write-Host 'Executando instalador do Chrome...' -ForegroundColor Yellow
        Start-Process $installer -Wait
        Remove-Item $installer -Force
        
        Start-Sleep 10
        
        if (Test-Path $chromeExeUser) {
            $chromeExe = $chromeExeUser
            Write-Host 'Chrome instalado com sucesso!' -ForegroundColor Green
        }
    }
    catch {
        Write-Host "Erro ao instalar Chrome: $($_.Exception.Message)" -ForegroundColor Red
    }
} else {
    if (Test-Path $chromeExe) {
        Write-Host 'Chrome encontrado (instalação global)' -ForegroundColor Green
    } else {
        $chromeExe = $chromeExeUser
        Write-Host 'Chrome encontrado (instalação do usuário)' -ForegroundColor Green
    }
}

# ===== FECHAR CHROME =====
Get-Process chrome -ErrorAction SilentlyContinue | Stop-Process -Force
Start-Sleep 2

# ===== CONFIGURAR CHROME =====
Write-Host 'Configurando Chrome...' -ForegroundColor Yellow

try {
    if (!(Test-Path $chromePolicyPath)) {
        New-Item -Path $chromePolicyPath -Force | Out-Null
    }

    Set-ItemProperty -Path $chromePolicyPath -Name 'RestoreOnStartup' -Value 4 -Type DWord
    Set-ItemProperty -Path $chromePolicyPath -Name 'BookmarkBarEnabled' -Value 1 -Type DWord
    Set-ItemProperty -Path $chromePolicyPath -Name 'ShowHomeButton' -Value 1 -Type DWord
    Set-ItemProperty -Path $chromePolicyPath -Name 'PromptForDownloadLocation' -Value 1 -Type DWord

    $startupListPath = "$chromePolicyPath\RestoreOnStartupURLs"
    if (!(Test-Path $startupListPath)) {
        New-Item -Path $startupListPath -Force | Out-Null
    }

    Set-ItemProperty -Path $startupListPath -Name '1' -Value $StartupUrl1 -Type String
    Set-ItemProperty -Path $startupListPath -Name '2' -Value $StartupUrl2 -Type String

    Write-Host '✅ Chrome configurado!' -ForegroundColor Green
}
catch {
    Write-Host "❌ Erro ao configurar Chrome: $($_.Exception.Message)" -ForegroundColor Red
}

# ===== CONFIGURAR FAVORITOS =====
if ($HtmlBookmarksPath) {
    Write-Host 'Configurando favoritos...' -ForegroundColor Yellow
    
    $chromeDataPath = if (Test-Path "${env:LOCALAPPDATA}\Google\Chrome\User Data\Default") {
        "${env:LOCALAPPDATA}\Google\Chrome\User Data\Default"
    } else {
        "${env:APPDATA}\Google\Chrome\User Data\Default"
    }
    
    if (!(Test-Path $chromeDataPath)) {
        New-Item -Path $chromeDataPath -ItemType Directory -Force | Out-Null
    }
    
    $bookmarksJson = @"
{
   "checksum": "",
   "roots": {
      "bookmark_bar": {
         "children": [ ],
         "date_added": "13285088828535757",
         "date_modified": "0",
         "id": "1",
         "name": "Barra de favoritos",
         "type": "folder"
      },
      "other": {
         "children": [ ],
         "date_added": "13285088828535758",
         "date_modified": "0",
         "id": "2",
         "name": "Outros favoritos",
         "type": "folder"
      }
   },
   "version": 1
}
"@
    
    $bookmarksJson | Out-File "$chromeDataPath\Bookmarks" -Encoding UTF8
    Write-Host '✅ Estrutura de favoritos criada!' -ForegroundColor Green
}

# ===== CONFIGURAR EDGE =====
Write-Host 'Configurando Edge...' -ForegroundColor Yellow

try {
    if (!(Test-Path $edgePolicyPath)) {
        New-Item -Path $edgePolicyPath -Force | Out-Null
    }

    Set-ItemProperty -Path $edgePolicyPath -Name 'RestoreOnStartup' -Value 4 -Type DWord
    Set-ItemProperty -Path $edgePolicyPath -Name 'FavoritesBarEnabled' -Value 1 -Type DWord
    Set-ItemProperty -Path $edgePolicyPath -Name 'PromptForDownloadLocation' -Value 1 -Type DWord

    $edgeStartupListPath = "$edgePolicyPath\RestoreOnStartupURLs"
    if (!(Test-Path $edgeStartupListPath)) {
        New-Item -Path $edgeStartupListPath -Force | Out-Null
    }

    Set-ItemProperty -Path $edgeStartupListPath -Name '1' -Value $StartupUrl1 -Type String
    Set-ItemProperty -Path $edgeStartupListPath -Name '2' -Value $StartupUrl2 -Type String

    Write-Host '✅ Edge configurado!' -ForegroundColor Green
}
catch {
    Write-Host "❌ Erro ao configurar Edge: $($_.Exception.Message)" -ForegroundColor Red
}

# ===== DEFINIR NAVEGADOR PADRÃO =====
Write-Host 'Definindo Chrome como padrão...' -ForegroundColor Yellow

try {
    Set-ItemProperty -Path 'HKCU:\Software\Microsoft\Windows\Shell\Associations\UrlAssociations\http\UserChoice' -Name 'ProgId' -Value 'ChromeHTML' -Force -ErrorAction SilentlyContinue
    Set-ItemProperty -Path 'HKCU:\Software\Microsoft\Windows\Shell\Associations\UrlAssociations\https\UserChoice' -Name 'ProgId' -Value 'ChromeHTML' -Force -ErrorAction SilentlyContinue
    
    Write-Host '✅ Chrome definido como padrão!' -ForegroundColor Green
}
catch {
    Write-Host '⚠️  Para definir como padrão, vá em Configurações > Aplicativos padrão' -ForegroundColor Yellow
}

# ===== VERIFICAR ATUALIZAÇÕES =====
if (Test-Path $chromeExe) {
    Write-Host 'Iniciando Chrome para aplicar configurações...' -ForegroundColor Yellow
    Start-Process $chromeExe -ArgumentList '--no-first-run --disable-default-apps' -WindowStyle Minimized
    Start-Sleep 5
    Get-Process chrome -ErrorAction SilentlyContinue | Stop-Process -Force
}

# ===== FINALIZAÇÃO =====
Write-Host "`n=== CONFIGURAÇÃO CONCLUÍDA ===" -ForegroundColor Green
Write-Host '✅ Configurações aplicadas ao Chrome e Edge' -ForegroundColor White
Write-Host "✅ URLs de inicialização: $StartupUrl1 e $StartupUrl2" -ForegroundColor White
Write-Host '✅ Prompt de download habilitado' -ForegroundColor White

if ($HtmlBookmarksPath) {
    Write-Host '`n📋 Para importar favoritos completamente:' -ForegroundColor Cyan
    Write-Host '   1. Abra o Chrome' -ForegroundColor White
    Write-Host '   2. Pressione Ctrl+Shift+O (Gerenciador de favoritos)' -ForegroundColor White
    Write-Host '   3. Clique nos 3 pontos > Importar favoritos' -ForegroundColor White
    Write-Host "   4. Selecione: $HtmlBookmarksPath" -ForegroundColor White
}

Write-Host '`nScript executado com sucesso!' -ForegroundColor Green
Write-Host 'Pressione qualquer tecla para sair...' -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey('NoEcho,IncludeKeyDown')