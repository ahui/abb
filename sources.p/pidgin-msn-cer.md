Title: Pidgin MSN证书链错误解决办法
Date: 2010-11-19 16:48
Author: ahui
Category: 网络
Tags: Network
Slug: pidgin-msn-cer

win7下把C:\\Users\\[用户名]\\AppData\\Roaming\\.purple\\certificates\\x509\\tls\_peers  
下的omega.contacts.msn.com文件内容替换成下面内容.并加上只读属性.  
或者在 工具-\>证书里,替换掉同名证书.

-----BEGIN CERTIFICATE-----  
MIIGeDCCBWCgAwIBAgIKfdrgSQAIAAHIuTANBgkqhkiG9w0BAQUFADCBizETMBEG  
CgmSJomT8ixkARkWA2NvbTEZMBcGCgmSJomT8ixkARkWCW1pY3Jvc29mdDEUMBIG  
CgmSJomT8ixkARkWBGNvcnAxFzAVBgoJkiaJk/IsZAEZFgdyZWRtb25kMSowKAYD  
VQQDEyFNaWNyb3NvZnQgU2VjdXJlIFNlcnZlciBBdXRob3JpdHkwHhcNMTAxMTE1  
MjEyODE5WhcNMTIxMTE0MjEyODE5WjB2MQswCQYDVQQGEwJVUzELMAkGA1UECBMC  
V0ExEDAOBgNVBAcTB1JlZG1vbmQxDDAKBgNVBAoTA01TTjEdMBsGA1UECxMUTVNO  
IENvbnRhY3QgU2VydmljZXMxGzAZBgNVBAMMEiouY29udGFjdHMubXNuLmNvbTCC  
ASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAJnXhdENETaZ8YFfenWCuky3  
Fke/oWgUOEbgvaRuZusd2LnvoSiqH++2lkV0JJlIQ+7jLLN8MY7VhlHQmkLC3x44  
KZn2IktMVgTBGMKnvbyYVAnRsjt/rVhQrQeHVEQzv5WXx//3FKmXWAuJiuRj9PZ2  
KsNqPJgaaa5cuOu4oynO9fH5/ZtJIeUf7bC4Wu++o7jTu5zOhIa7R1buE9FXFF33  
vQ1vHi4p9zR2Pi/i2nUpEnzeNCLl/8F/Tf+658SvIC4EzxrYcj+fit6sAnNUfsOE  
1SIk9YLD+tS0fln1afbcDvH0ib5Xm7u2/o6ZmxQU0mrAkfQectsKpZLJj03neBsC  
AwEAAaOCAvAwggLsMAsGA1UdDwQEAwIEsDBEBgkqhkiG9w0BCQ8ENzA1MA4GCCqG  
SIb3DQMCAgIAgDAOBggqhkiG9w0DBAICAIAwBwYFKw4DAgcwCgYIKoZIhvcNAwcw  
HQYDVR0lBBYwFAYIKwYBBQUHAwIGCCsGAQUFBwMBMB0GA1UdDgQWBBRciAVJ/Vsj  
sAlZoNG/Zs+rILsPNDAfBgNVHSMEGDAWgBQIQuPbThFm87UIxUDbVXwzRhGDODCC  
AQoGA1UdHwSCAQEwgf4wgfuggfiggfWGWGh0dHA6Ly9tc2NybC5taWNyb3NvZnQu  
Y29tL3BraS9tc2NvcnAvY3JsL01pY3Jvc29mdCUyMFNlY3VyZSUyMFNlcnZlciUy  
MEF1dGhvcml0eSg4KS5jcmyGVmh0dHA6Ly9jcmwubWljcm9zb2Z0LmNvbS9wa2kv  
bXNjb3JwL2NybC9NaWNyb3NvZnQlMjBTZWN1cmUlMjBTZXJ2ZXIlMjBBdXRob3Jp  
dHkoOCkuY3JshkFodHRwOi8vY29ycHBraS9jcmwvTWljcm9zb2Z0JTIwU2VjdXJl  
JTIwU2VydmVyJTIwQXV0aG9yaXR5KDgpLmNybDCBvwYIKwYBBQUHAQEEgbIwga8w  
XgYIKwYBBQUHMAKGUmh0dHA6Ly93d3cubWljcm9zb2Z0LmNvbS9wa2kvbXNjb3Jw  
L01pY3Jvc29mdCUyMFNlY3VyZSUyMFNlcnZlciUyMEF1dGhvcml0eSg4KS5jcnQw  
TQYIKwYBBQUHMAKGQWh0dHA6Ly9jb3JwcGtpL2FpYS9NaWNyb3NvZnQlMjBTZWN1  
cmUlMjBTZXJ2ZXIlMjBBdXRob3JpdHkoOCkuY3J0MD8GCSsGAQQBgjcVBwQyMDAG  
KCsGAQQBgjcVCIPPiU2t8gKFoZ8MgvrKfYHh+3SBT4PC7YUIjqnShWMCAWQCAQow  
JwYJKwYBBAGCNxUKBBowGDAKBggrBgEFBQcDAjAKBggrBgEFBQcDATANBgkqhkiG  
9w0BAQUFAAOCAQEAbbWUY/5r/Tv/kefqNUT5aGVejrkbG4229gnJLcv+uQTEg0Gg  
xfvLr77N1z2j57FameJwz6DeTRbK8MYVPoP+z5o4vM3F3GxLm7aBklYQ/7G0TIp/  
13z01a5aBGvZH8umzex3YrAnhJEcucSN5WaT6r9uwT7imdbsCgfFPdiIgS5iHdcl  
k/3QSpau+4/XZgh/8V/FMN9KEFYGvEhMb5EVzKJ8pqF9Jy9Mfzqev3BtSREiljCt  
lJuiRamxWgQoeNVTAI+J2YAsD8Qon1iZiHl08uHdgXWZiGDtLPcd9aIiL7/vi/+D  
7w3bhyHPFr+/13BCIWSfKnSRj/g6YoHnhF4gyQ==  
-----END CERTIFICATE-----

证书原地址:  
http://heiher.info/sftp/files/omega.contacts.msn.com  
or  
http://webupd8.googlecode.com/files/omega.contacts.msn.com