$user = $env:USERNAME

New-NetFirewallRule –Name "BaseBrd" -DisplayName "2D Builder" -Profile Domain,Public,Private -Enabled True -Protocol TCP -Program C:\Users\$user\Desktop\Winlog_2.2\Srv_Winlog_2.2\Srv_Winlog_2.2.exe
