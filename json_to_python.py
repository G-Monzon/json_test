"""
WIP
"""
import json

# String de prueba
string_prueba = '''{
    "totalEmitidas": "$200,000.14",
    "facturasEmitidas": [
        {
            "folio": "AD405471-340F-4205-B0E5-AC02DA214638",
            "rfcEmisor": "XXXX999999XXX",
            "razonSocialEmisor": "JUAN ALBERTO PEREZ GONZALEZ",
            "rfcReceptor": "XXXX999999XXX",
            "razonSocialReceptor": "LA EMPRESA, S.A. DE C.V.",
            "fechaEmision": "2022-06-01T19:55:50",
            "fechaCertificacion": "2022-06-01T19:56:43",
            "pac": "SAT970701NN3",
            "monto": "$200,000.14",
            "efecto": "Ingreso",
            "estatus": "Cancelable con aceptación",
            "estado": "Vigente",
            "estatusProcesoCancelacion": null,
            "fechaProcesoCancelacion": null,
            "rfcCuentaTerceros": null,
            "motivo": null,
            "folioSustitucion": null,
            "xml": "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz48Y2ZkaTpDb21wcm9iYW50ZSB4bWxuczp4c2k9Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1hLWluc3RhbmNlIiB4bWxuczp0ZmQ9Imh0dHA6Ly93d3cuc2F0LmdvYi5teC9UaW1icmVGaXNjYWxEaWdpdGFsIiB4c2k6c2NoZW1hTG9jYXRpb249Imh0dHA6Ly93d3cuc2F0LmdvYi5teC9jZmQvMyBodHRwOi8vd3d3LnNhdC5nb2IubXgvc2l0aW9faW50ZXJuZXQvY2ZkLzMvY2ZkdjMzLnhzZCIgVmVyc2lvbj0iMy4zIiBTZXJpZT0iQSIgRm9saW89IjI3NTEiIEZlY2hhPSIyMDIyLTA3LTI5VDE1OjI5OjU4IiBTZWxsbz0iZnBHamc2VTFDeC85OGpySUE0ODgyc3NDbG04eEgvMi9OdEdkSkcrd0dIaHU4L2VwbVY4RnZmbEdjNUNHc1UzMU9VbTdPSmJUdWluc1NwdXM5bkw2NUIxN2xMcWg0R1l4WFFoeVVneU5hdzlpYTZRU21YQzVkTkpNSjdxWkNMdWU0eXRNYVE2ZU9mN01VcWpCUkhsZExtTVhpTEpxaW9lWUR0SDlubjBZTVcwVXpsQ2QvdXFibUd4Y2cyb2dsWVRVQmEwWUVNOE85cE0yTU1ReUxHa3RENGIzRDJGY09MZ3lMemt1QWg5NllGa3ljZmhJbWYwaGVOSXRWYlNKc2FZU29NZkl0R2JoVDZEWStnWUIxOE1xS20xVmIrYlduY1lxYUZnNjU0MGY2Q1dUNTVSZVVvVnp4NERyTUE0Z3RwNVNqUUVINGpnZDQwVjM4a2VZSjJMZkJBPT0iIEZvcm1hUGFnbz0iMDMiIE5vQ2VydGlmaWNhZG89IjAwMDAxMDAwMDAwNTAwMzU0Mzk5IiBDZXJ0aWZpY2Fkbz0iTUlJR0JEQ0NBK3lnQXdJQkFnSVVNREF3TURFd01EQXdNREExTURBek5UUXpPVGt3RFFZSktvWklodmNOQVFFTEJRQXdnZ0dFTVNBd0hnWURWUVFEREJkQlZWUlBVa2xFUVVRZ1EwVlNWRWxHU1VOQlJFOVNRVEV1TUN3R0ExVUVDZ3dsVTBWU1ZrbERTVThnUkVVZ1FVUk5TVTVKVTFSU1FVTkpUMDRnVkZKSlFsVlVRVkpKUVRFYU1CZ0dBMVVFQ3d3UlUwRlVMVWxGVXlCQmRYUm9iM0pwZEhreEtqQW9CZ2txaGtpRzl3MEJDUUVXRzJOdmJuUmhZM1J2TG5SbFkyNXBZMjlBYzJGMExtZHZZaTV0ZURFbU1DUUdBMVVFQ1F3ZFFWWXVJRWhKUkVGTVIwOGdOemNzSUVOUFRDNGdSMVZGVWxKRlVrOHhEakFNQmdOVkJCRU1CVEEyTXpBd01Rc3dDUVlEVlFRR0V3Sk5XREVaTUJjR0ExVUVDQXdRUTBsVlJFRkVJRVJGSUUxRldFbERUekVUTUJFR0ExVUVCd3dLUTFWQlZVaFVSVTFQUXpFVk1CTUdBMVVFTFJNTVUwRlVPVGN3TnpBeFRrNHpNVnd3V2dZSktvWklodmNOQVFrQ0UwMXlaWE53YjI1ellXSnNaVG9nUVVSTlNVNUpVMVJTUVVOSlQwNGdRMFZPVkZKQlRDQkVSU0JUUlZKV1NVTkpUMU1nVkZKSlFsVlVRVkpKVDFNZ1FVd2dRMDlPVkZKSlFsVlpSVTVVUlRBZUZ3MHhPVEEyTWpBeU1ERXhOVEphRncweU16QTJNakF5TURFeE5USmFNSUhTTVNZd0pBWURWUVFERXgxR1NVNUJUazlXUVNCVFFWQkpJRVJGSUVOV0lGTlBSazlOSUVWT1VqRW1NQ1FHQTFVRUtSTWRSa2xPUVU1UFZrRWdVMEZRU1NCRVJTQkRWaUJUVDBaUFRTQkZUbEl4SmpBa0JnTlZCQW9USFVaSlRrRk9UMVpCSUZOQlVFa2dSRVVnUTFZZ1UwOUdUMDBnUlU1U01TVXdJd1lEVlFRdEV4eEdTVTR4TkRBNU16QkhVallnTHlCTlJWTldPRFF4TURBMVJVY3dNUjR3SEFZRFZRUUZFeFVnTHlCTlJWTldPRFF4TURBMVNFTklUbEJETURReEVUQVBCZ05WQkFzVENFWkpUa0ZPVDFaQk1JSUJJakFOQmdrcWhraUc5dzBCQVFFRkFBT0NBUThBTUlJQkNnS0NBUUVBaXh3RzU0QXd6WWdTV3UrR2ZxN1hlUVVBdlUrQjJtemlDM0RyOW9SSXorMm8zMGZCOTd3UUhHcVJTZHo5QU5PbHRidmJGcjg0V3Fib09qWTdac0R1YXlaa0tFSG51VTFsZ2dpM2I0UFJDcmt0dEZYbjlxaC9pTkNXRUFJTkVWNzVPQWhzOFp5RDQ2MEJPTVdwUk1UOUR3SThmK0RlRjUvRldWQnlzUWZDdmtMLzd2dDhBeVJ2VmF6TU8vcTcyVGIzMXMzZEFkRzMvbFpGRnlsRTlCd1BQeURUWGNBZU5ZSm1DNDg3VS9QU2I0M1phNUFGUWNIUENldHludnlOb0UwK3lOMGRlMUltS3hyVVZkd09Ybjc0L3loWXQreEdNL3pHR3owN2NaOHlnRldGaTBQUVRYZ3oyMW1GNXRLRTU2TmlyVlNmcFVDR1c0V2g5cDZlcG1NMjVRSURBUUFCb3gwd0d6QU1CZ05WSFJNQkFmOEVBakFBTUFzR0ExVWREd1FFQXdJR3dEQU5CZ2txaGtpRzl3MEJBUXNGQUFPQ0FnRUFreXBCV3BXbUdrU2xCNzd1ZEhOTFlzWkR5cDF2VTFyQjlEMmNOUE85VWtHRjkwZSs2MFdOMFUwQlhmdytSSHFXamRvdEl4azhEV3V2UWNmU1hRNlBFSTlDVVQ3VDRvamsveGVnL082Q3U3djd4aGNhaGNWK3c2b2hxRVV4VUlBWDlJNElCaU9ZRjdBZjI5TjZpeUlPclU2eFlMd1BRTU1UTWZmcERLWFlQd0lsUU5UWFBXWHBhUllaU28yZnFmck43UmtBUmR3UVM3NU8vSTFROXdqTkNOTmFuWUtUNytHT09HTjY0YzhPY3o4YlZvVjRsa21aS2F4alNlUjhUSVRFR0tEQ0dxdVdrOUZqM1Vlanpwb2JqUTJxMVpYWG5xa0lrNDU4UHBEVGliNDk2aEFRYldDYndkT2ZxeWVzZ0owUTZaeWthUmpQMVptNDkzYS9idCttemUvd1lBYzBsSiswRVBJRm5ISGpyTWdOd1lvRUN5K1hpb04zZlBxNEh2WWtLWUwzMTdvR0xaR1I1OFlXMDNaZnRiOXNvRzdaRDkwWnVoQ2xoN05hMkxMZnpIUFNwS2VzMkl0N0g3cHV2SGw4L3ZZanlJS3FmQmtOelNBQUlOUDFkK25QRkhDY1JHNVpXSTNuM25pZ0JsQ1NZUU40QnQxelBJd0JxYXlnZWVlWnZuSzNydHJXT29oMGxmbWgrNk1DNENKL3dRU21uUDRWQVR3ZlF5anRNb0tmdGlqZkxDUFh0Q085cTJjNEt4aWl5R1RqcndBQ1YwY2FmakdTRXVWVUI3eGhsMTdHSjBRVE5aY0xnb05FSERtRlk3T2FScDVaS2JudGUzQkt6UVEyVmJNY3dwSzNxeTdPYWJmZHBPS3NXdnlhMXlDQXVsVDZxazVvWmFybjJUOD0iIFN1YlRvdGFsPSI5MzY2Ljg0IiBNb25lZGE9Ik1YTiIgVG90YWw9IjkzNjYuODQiIFRpcG9EZUNvbXByb2JhbnRlPSJJIiBNZXRvZG9QYWdvPSJQVUUiIEx1Z2FyRXhwZWRpY2lvbj0iMzExMTAiIHhtbG5zOmNmZGk9Imh0dHA6Ly93d3cuc2F0LmdvYi5teC9jZmQvMyI+PGNmZGk6RW1pc29yIFJmYz0iRklOMTQwOTMwR1I2IiBOb21icmU9IkZJTkFOT1ZBIFNBUEkgREUgQ1YgU09GT00gRU5SIiBSZWdpbWVuRmlzY2FsPSI2MDEiIC8+PGNmZGk6UmVjZXB0b3IgUmZjPSJDQUVNODAwODMxQUUwIiBOb21icmU9Ik1pcmlhbSBHdWFkYWx1cGUgQ2hhcGFycm8gRXN0cmFkYSIgVXNvQ0ZEST0iRzAzIiAvPjxjZmRpOkNvbmNlcHRvcz48Y2ZkaTpDb25jZXB0byBDbGF2ZVByb2RTZXJ2PSI4NDEwMTcwMyIgTm9JZGVudGlmaWNhY2lvbj0iODQxMDE3MDMiIENhbnRpZGFkPSIxIiBDbGF2ZVVuaWRhZD0iRTQ4IiBVbmlkYWQ9IkU0OCIgRGVzY3JpcGNpb249IkludGVyZXNlcyBkZXZlbmdhZG9zIGRlbCBtZXMgZGUgSnVsaW8gZGVsIDIwMjIgTUdDSEUgMjgtQ1QxLTI1IiBWYWxvclVuaXRhcmlvPSI3NDY2Ljg0IiBJbXBvcnRlPSI3NDY2Ljg0Ij48Y2ZkaTpJbXB1ZXN0b3M+PGNmZGk6VHJhc2xhZG9zPjxjZmRpOlRyYXNsYWRvIEJhc2U9Ijc0NjYuODQiIEltcHVlc3RvPSIwMDIiIFRpcG9GYWN0b3I9IlRhc2EiIFRhc2FPQ3VvdGE9IjAuMDAwMDAwIiBJbXBvcnRlPSIwLjAwIiAvPjwvY2ZkaTpUcmFzbGFkb3M+PC9jZmRpOkltcHVlc3Rvcz48L2NmZGk6Q29uY2VwdG8+PGNmZGk6Q29uY2VwdG8gQ2xhdmVQcm9kU2Vydj0iODQxMDE3MDMiIE5vSWRlbnRpZmljYWNpb249Ijg0MTAxNzAzIiBDYW50aWRhZD0iMSIgQ2xhdmVVbmlkYWQ9IkU0OCIgVW5pZGFkPSJFNDgiIERlc2NyaXBjaW9uPSJJbnRlcmVzZXMgbW9yYXRvcmlvcyBkZWwgbWVzIGRlIEp1bGlvIGRlbCAyMDIyIE1HQ0hFIDI4LUNUMS0yNSIgVmFsb3JVbml0YXJpbz0iMTkwMC4wMCIgSW1wb3J0ZT0iMTkwMC4wMCI+PGNmZGk6SW1wdWVzdG9zPjxjZmRpOlRyYXNsYWRvcz48Y2ZkaTpUcmFzbGFkbyBCYXNlPSIxOTAwLjAwIiBJbXB1ZXN0bz0iMDAyIiBUaXBvRmFjdG9yPSJUYXNhIiBUYXNhT0N1b3RhPSIwLjAwMDAwMCIgSW1wb3J0ZT0iMC4wMCIgLz48L2NmZGk6VHJhc2xhZG9zPjwvY2ZkaTpJbXB1ZXN0b3M+PC9jZmRpOkNvbmNlcHRvPjwvY2ZkaTpDb25jZXB0b3M+PGNmZGk6SW1wdWVzdG9zIFRvdGFsSW1wdWVzdG9zVHJhc2xhZGFkb3M9IjAuMDAiPjxjZmRpOlRyYXNsYWRvcz48Y2ZkaTpUcmFzbGFkbyBJbXB1ZXN0bz0iMDAyIiBUaXBvRmFjdG9yPSJUYXNhIiBUYXNhT0N1b3RhPSIwLjAwMDAwMCIgSW1wb3J0ZT0iMC4wMCIgLz48L2NmZGk6VHJhc2xhZG9zPjwvY2ZkaTpJbXB1ZXN0b3M+PGNmZGk6Q29tcGxlbWVudG8+PHRmZDpUaW1icmVGaXNjYWxEaWdpdGFsIHhzaTpzY2hlbWFMb2NhdGlvbj0iaHR0cDovL3d3dy5zYXQuZ29iLm14L1RpbWJyZUZpc2NhbERpZ2l0YWwgaHR0cDovL3d3dy5zYXQuZ29iLm14L3NpdGlvX2ludGVybmV0L2NmZC9UaW1icmVGaXNjYWxEaWdpdGFsL1RpbWJyZUZpc2NhbERpZ2l0YWx2MTEueHNkIiBWZXJzaW9uPSIxLjEiIFVVSUQ9ImRiNjk3OTMwLTEwN2EtNDE4Ni04MWUwLTJlM2I1Y2M4N2IwMyIgRmVjaGFUaW1icmFkbz0iMjAyMi0wNy0yOVQxNjoyOTo1OCIgUmZjUHJvdkNlcnRpZj0iTFNPMTMwNjE4OVI1IiBTZWxsb0NGRD0iZnBHamc2VTFDeC85OGpySUE0ODgyc3NDbG04eEgvMi9OdEdkSkcrd0dIaHU4L2VwbVY4RnZmbEdjNUNHc1UzMU9VbTdPSmJUdWluc1NwdXM5bkw2NUIxN2xMcWg0R1l4WFFoeVVneU5hdzlpYTZRU21YQzVkTkpNSjdxWkNMdWU0eXRNYVE2ZU9mN01VcWpCUkhsZExtTVhpTEpxaW9lWUR0SDlubjBZTVcwVXpsQ2QvdXFibUd4Y2cyb2dsWVRVQmEwWUVNOE85cE0yTU1ReUxHa3RENGIzRDJGY09MZ3lMemt1QWg5NllGa3ljZmhJbWYwaGVOSXRWYlNKc2FZU29NZkl0R2JoVDZEWStnWUIxOE1xS20xVmIrYlduY1lxYUZnNjU0MGY2Q1dUNTVSZVVvVnp4NERyTUE0Z3RwNVNqUUVINGpnZDQwVjM4a2VZSjJMZkJBPT0iIE5vQ2VydGlmaWNhZG9TQVQ9IjAwMDAxMDAwMDAwNTA5ODQ2NjYzIiBTZWxsb1NBVD0iZWNEeVFBdHE2NXZEK3ZRWFJReE5kQThIV2U2STUxMVZ5M3Y0L2RCelVlSHpueHU0c1hDZUpVSjhSQkF6MGNCZUM5a3BKZG1nSU1OKzRpalJSeFFhajRQeGNoWUZVMjZGQ05NeHluYnYrUDhFT3pjcjZDTmVUMVdQdW44bi9uS0JLYU9NcWRHTzE0Nkkzdjd6KzF5cGNZNlR5N2Fzc0RPd2VDeVlBL3MzbFpTTXR4ZDhCVTNLcnhFSDZSbHpOSkovZUNHeTBDU0JzZ01TdTBKRkdpZWxaN1NZWEJZeEFmVmFtRlp1WXdOb2Q3UTdCZUVkZDRGdGtBaC9hTWErY0lMbHZVWWwwWDNTS2xzRDZoQXhYZ0VsZEh5djJ4RTIwcVVnSWdtUHBqUlZQNWJOanZ6RVJsOWo4OUF1SkxLU0JudlBnSDBuSWw4cUhBU2M0SGFPS3c5NzBnPT0iIC8+PC9jZmRpOkNvbXBsZW1lbnRvPjwvY2ZkaTpDb21wcm9iYW50ZT4=",
            "pdf": "Base64 del PDF"
        }
    ],
    "totalRecibidas": "$2,795.60",
    "totalDiferencia": "$197,204.54",
    "facturasRecibidas": [
        {
            "folio": "E5ECDC9E-AF7F-4836-A0F8-93C5B9C1769A",
            "rfcEmisor": "XXXX999999XXX",
            "razonSocialEmisor": "BBVA MEXICO, S.A., INSTITUCION DE BANCA MULTIPLE, GRUPO FINANCIERO BBVA MEXICO.",
            "rfcReceptor": "XXXX999999XXX",
            "razonSocialReceptor": "JUAN ALBERTO PEREZ GONZALEZ",
            "fechaEmision": "2022-06-23T01:13:33",
            "fechaCertificacion": "2022-06-23T06:35:01",
            "pac": "CEC961028A98",
            "monto": "$2,795.60",
            "efecto": "Ingreso",
            "estatus": "Cancelable sin aceptación",
            "estado": "Vigente",
            "estatusProcesoCancelacion": null,
            "fechaProcesoCancelacion": null,
            "rfcCuentaTerceros": null,
            "xml": "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz48Y2ZkaTpDb21wcm9iYW50ZSB4bWxuczp4c2k9Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1hLWluc3RhbmNlIiB4bWxuczp0ZmQ9Imh0dHA6Ly93d3cuc2F0LmdvYi5teC9UaW1icmVGaXNjYWxEaWdpdGFsIiB4c2k6c2NoZW1hTG9jYXRpb249Imh0dHA6Ly93d3cuc2F0LmdvYi5teC9jZmQvMyBodHRwOi8vd3d3LnNhdC5nb2IubXgvc2l0aW9faW50ZXJuZXQvY2ZkLzMvY2ZkdjMzLnhzZCIgVmVyc2lvbj0iMy4zIiBTZXJpZT0iRSIgRm9saW89IjE5MyIgRmVjaGE9IjIwMjItMDctMjlUMTI6NTE6NTMiIFNlbGxvPSJDT1dxbW5DbElSem9tRXA5VHo2OExSZ0d2WFdzRWQyMkJGMnZJc2FOWGkrL3pyNmpYajkra1IyUVBPWEozcHRuRFVIR0NQRy9lSXFVdk1ZRkNXQlBROW5ZSXNlT2RJcWRiSmh0cHpvYkl0cFdtb04wU0RLYWNKTXFNN0pQWjQzcGJuNHRjcXdSZ3pZdU9EOURNK0JZaVlrd0dLMytxbTBZRGxIeU8raVdoU2d2cnhmcms5QVhVTm4zaGw4cCs0aWh5TFhCQVduY0NGakxFMTJnZ1M5Yk9LcmlCVlNjdnczZjAzWjU0cTBxWnhtbmhzVDVuSGpscEd5ckR4MTVrOWhET0F4RU9YaFoxZUtWQXBpc3RPcWN0ekxFWlRma3VGSFc4cmJKVUQ5SDBMcnU1Z0JHbXhpQUplS1NCY3R5cy9uTXVvVVJhV0N6NDNLcHJCWFBrUmZ0Y1E9PSIgRm9ybWFQYWdvPSI5OSIgTm9DZXJ0aWZpY2Fkbz0iMDAwMDEwMDAwMDA1MDAzNTQzOTkiIENlcnRpZmljYWRvPSJNSUlHQkRDQ0EreWdBd0lCQWdJVU1EQXdNREV3TURBd01EQTFNREF6TlRRek9Ua3dEUVlKS29aSWh2Y05BUUVMQlFBd2dnR0VNU0F3SGdZRFZRUUREQmRCVlZSUFVrbEVRVVFnUTBWU1ZFbEdTVU5CUkU5U1FURXVNQ3dHQTFVRUNnd2xVMFZTVmtsRFNVOGdSRVVnUVVSTlNVNUpVMVJTUVVOSlQwNGdWRkpKUWxWVVFWSkpRVEVhTUJnR0ExVUVDd3dSVTBGVUxVbEZVeUJCZFhSb2IzSnBkSGt4S2pBb0Jna3Foa2lHOXcwQkNRRVdHMk52Ym5SaFkzUnZMblJsWTI1cFkyOUFjMkYwTG1kdllpNXRlREVtTUNRR0ExVUVDUXdkUVZZdUlFaEpSRUZNUjA4Z056Y3NJRU5QVEM0Z1IxVkZVbEpGVWs4eERqQU1CZ05WQkJFTUJUQTJNekF3TVFzd0NRWURWUVFHRXdKTldERVpNQmNHQTFVRUNBd1FRMGxWUkVGRUlFUkZJRTFGV0VsRFR6RVRNQkVHQTFVRUJ3d0tRMVZCVlVoVVJVMVBRekVWTUJNR0ExVUVMUk1NVTBGVU9UY3dOekF4VGs0ek1Wd3dXZ1lKS29aSWh2Y05BUWtDRTAxeVpYTndiMjV6WVdKc1pUb2dRVVJOU1U1SlUxUlNRVU5KVDA0Z1EwVk9WRkpCVENCRVJTQlRSVkpXU1VOSlQxTWdWRkpKUWxWVVFWSkpUMU1nUVV3Z1EwOU9WRkpKUWxWWlJVNVVSVEFlRncweE9UQTJNakF5TURFeE5USmFGdzB5TXpBMk1qQXlNREV4TlRKYU1JSFNNU1l3SkFZRFZRUURFeDFHU1U1QlRrOVdRU0JUUVZCSklFUkZJRU5XSUZOUFJrOU5JRVZPVWpFbU1DUUdBMVVFS1JNZFJrbE9RVTVQVmtFZ1UwRlFTU0JFUlNCRFZpQlRUMFpQVFNCRlRsSXhKakFrQmdOVkJBb1RIVVpKVGtGT1QxWkJJRk5CVUVrZ1JFVWdRMVlnVTA5R1QwMGdSVTVTTVNVd0l3WURWUVF0RXh4R1NVNHhOREE1TXpCSFVqWWdMeUJOUlZOV09EUXhNREExUlVjd01SNHdIQVlEVlFRRkV4VWdMeUJOUlZOV09EUXhNREExU0VOSVRsQkRNRFF4RVRBUEJnTlZCQXNUQ0VaSlRrRk9UMVpCTUlJQklqQU5CZ2txaGtpRzl3MEJBUUVGQUFPQ0FROEFNSUlCQ2dLQ0FRRUFpeHdHNTRBd3pZZ1NXdStHZnE3WGVRVUF2VStCMm16aUMzRHI5b1JJeisybzMwZkI5N3dRSEdxUlNkejlBTk9sdGJ2YkZyODRXcWJvT2pZN1pzRHVheVprS0VIbnVVMWxnZ2kzYjRQUkNya3R0RlhuOXFoL2lOQ1dFQUlORVY3NU9BaHM4WnlENDYwQk9NV3BSTVQ5RHdJOGYrRGVGNS9GV1ZCeXNRZkN2a0wvN3Z0OEF5UnZWYXpNTy9xNzJUYjMxczNkQWRHMy9sWkZGeWxFOUJ3UFB5RFRYY0FlTllKbUM0ODdVL1BTYjQzWmE1QUZRY0hQQ2V0eW52eU5vRTAreU4wZGUxSW1LeHJVVmR3T1huNzQveWhZdCt4R00vekdHejA3Y1o4eWdGV0ZpMFBRVFhnejIxbUY1dEtFNTZOaXJWU2ZwVUNHVzRXaDlwNmVwbU0yNVFJREFRQUJveDB3R3pBTUJnTlZIUk1CQWY4RUFqQUFNQXNHQTFVZER3UUVBd0lHd0RBTkJna3Foa2lHOXcwQkFRc0ZBQU9DQWdFQWt5cEJXcFdtR2tTbEI3N3VkSE5MWXNaRHlwMXZVMXJCOUQyY05QTzlVa0dGOTBlKzYwV04wVTBCWGZ3K1JIcVdqZG90SXhrOERXdXZRY2ZTWFE2UEVJOUNVVDdUNG9qay94ZWcvTzZDdTd2N3hoY2FoY1YrdzZvaHFFVXhVSUFYOUk0SUJpT1lGN0FmMjlONml5SU9yVTZ4WUx3UFFNTVRNZmZwREtYWVB3SWxRTlRYUFdYcGFSWVpTbzJmcWZyTjdSa0FSZHdRUzc1Ty9JMVE5d2pOQ05OYW5ZS1Q3K0dPT0dONjRjOE9jejhiVm9WNGxrbVpLYXhqU2VSOFRJVEVHS0RDR3F1V2s5RmozVWVqenBvYmpRMnExWlhYbnFrSWs0NThQcERUaWI0OTZoQVFiV0Nid2RPZnF5ZXNnSjBRNlp5a2FSalAxWm00OTNhL2J0K216ZS93WUFjMGxKKzBFUElGbkhIanJNZ053WW9FQ3krWGlvTjNmUHE0SHZZa0tZTDMxN29HTFpHUjU4WVcwM1pmdGI5c29HN1pEOTBadWhDbGg3TmEyTExmekhQU3BLZXMySXQ3SDdwdXZIbDgvdllqeUlLcWZCa056U0FBSU5QMWQrblBGSENjUkc1WldJM24zbmlnQmxDU1lRTjRCdDF6UEl3QnFheWdlZWVadm5LM3J0cldPb2gwbGZtaCs2TUM0Q0ovd1FTbW5QNFZBVHdmUXlqdE1vS2Z0aWpmTENQWHRDTzlxMmM0S3hpaXlHVGpyd0FDVjBjYWZqR1NFdVZVQjd4aGwxN0dKMFFUTlpjTGdvTkVIRG1GWTdPYVJwNVpLYm50ZTNCS3pRUTJWYk1jd3BLM3F5N09hYmZkcE9Lc1d2eWExeUNBdWxUNnFrNW9aYXJuMlQ4PSIgU3ViVG90YWw9IjEzMDQuOTEiIE1vbmVkYT0iTVhOIiBUb3RhbD0iMTMwNC45MSIgVGlwb0RlQ29tcHJvYmFudGU9IkkiIE1ldG9kb1BhZ289IlBQRCIgTHVnYXJFeHBlZGljaW9uPSIzMTExMCIgeG1sbnM6Y2ZkaT0iaHR0cDovL3d3dy5zYXQuZ29iLm14L2NmZC8zIj48Y2ZkaTpFbWlzb3IgUmZjPSJGSU4xNDA5MzBHUjYiIE5vbWJyZT0iRklOQU5PVkEgU0FQSSBERSBDViBTT0ZPTSBFTlIiIFJlZ2ltZW5GaXNjYWw9IjYwMSIgLz48Y2ZkaTpSZWNlcHRvciBSZmM9Ik1FQ0o4NTAzMjNSSTgiIE5vbWJyZT0iSnVhbiBDYXJsb3MgTWVzdGEgQ2FudHUiIFVzb0NGREk9IkcwMyIgLz48Y2ZkaTpDb25jZXB0b3M+PGNmZGk6Q29uY2VwdG8gQ2xhdmVQcm9kU2Vydj0iODQxMDE3MDMiIE5vSWRlbnRpZmljYWNpb249Ijg0MTAxNzAzIiBDYW50aWRhZD0iMSIgQ2xhdmVVbmlkYWQ9IkU0OCIgVW5pZGFkPSJFNDgiIERlc2NyaXBjaW9uPSJJbnRlcmVzZXMgZGV2ZW5nYWRvcyBkZWwgbWVzIGRlIEp1bGlvIGRlbCAyMDIyIEpDTUMgMTUwLVBRMS0wMSIgVmFsb3JVbml0YXJpbz0iMTMwNC45MSIgSW1wb3J0ZT0iMTMwNC45MSI+PGNmZGk6SW1wdWVzdG9zPjxjZmRpOlRyYXNsYWRvcz48Y2ZkaTpUcmFzbGFkbyBCYXNlPSIxMzA0LjkxIiBJbXB1ZXN0bz0iMDAyIiBUaXBvRmFjdG9yPSJUYXNhIiBUYXNhT0N1b3RhPSIwLjAwMDAwMCIgSW1wb3J0ZT0iMC4wMCIgLz48L2NmZGk6VHJhc2xhZG9zPjwvY2ZkaTpJbXB1ZXN0b3M+PC9jZmRpOkNvbmNlcHRvPjwvY2ZkaTpDb25jZXB0b3M+PGNmZGk6SW1wdWVzdG9zIFRvdGFsSW1wdWVzdG9zVHJhc2xhZGFkb3M9IjAuMDAiPjxjZmRpOlRyYXNsYWRvcz48Y2ZkaTpUcmFzbGFkbyBJbXB1ZXN0bz0iMDAyIiBUaXBvRmFjdG9yPSJUYXNhIiBUYXNhT0N1b3RhPSIwLjAwMDAwMCIgSW1wb3J0ZT0iMC4wMCIgLz48L2NmZGk6VHJhc2xhZG9zPjwvY2ZkaTpJbXB1ZXN0b3M+PGNmZGk6Q29tcGxlbWVudG8+PHRmZDpUaW1icmVGaXNjYWxEaWdpdGFsIHhzaTpzY2hlbWFMb2NhdGlvbj0iaHR0cDovL3d3dy5zYXQuZ29iLm14L1RpbWJyZUZpc2NhbERpZ2l0YWwgaHR0cDovL3d3dy5zYXQuZ29iLm14L3NpdGlvX2ludGVybmV0L2NmZC9UaW1icmVGaXNjYWxEaWdpdGFsL1RpbWJyZUZpc2NhbERpZ2l0YWx2MTEueHNkIiBWZXJzaW9uPSIxLjEiIFVVSUQ9IjEwODQzZDVjLWRiMmItNDk1My05OTNmLTUzMWEwYzMzMDQ5OSIgRmVjaGFUaW1icmFkbz0iMjAyMi0wNy0yOVQxMzo1MTo1NCIgUmZjUHJvdkNlcnRpZj0iTFNPMTMwNjE4OVI1IiBTZWxsb0NGRD0iQ09XcW1uQ2xJUnpvbUVwOVR6NjhMUmdHdlhXc0VkMjJCRjJ2SXNhTlhpKy96cjZqWGo5K2tSMlFQT1hKM3B0bkRVSEdDUEcvZUlxVXZNWUZDV0JQUTluWUlzZU9kSXFkYkpodHB6b2JJdHBXbW9OMFNES2FjSk1xTTdKUFo0M3BibjR0Y3F3Umd6WXVPRDlETStCWWlZa3dHSzMrcW0wWURsSHlPK2lXaFNndnJ4ZnJrOUFYVU5uM2hsOHArNGloeUxYQkFXbmNDRmpMRTEyZ2dTOWJPS3JpQlZTY3Z3M2YwM1o1NHEwcVp4bW5oc1Q1bkhqbHBHeXJEeDE1azloRE9BeEVPWGhaMWVLVkFwaXN0T3FjdHpMRVpUZmt1RkhXOHJiSlVEOUgwTHJ1NWdCR214aUFKZUtTQmN0eXMvbk11b1VSYVdDejQzS3ByQlhQa1JmdGNRPT0iIE5vQ2VydGlmaWNhZG9TQVQ9IjAwMDAxMDAwMDAwNTA5ODQ2NjYzIiBTZWxsb1NBVD0iS1c2ektrS1hFM2dzRytTNGFnUngvSk11UFU5Ly9NemphdGJHamtHck5qV0ZlNmtrYmZkSU1pS3VEMzB6aDFQcElwUTB5d2NOaE11OENoTjYyYVpUSmlRRnZJQ3dFd3BlMGJMYXhINTlJam9HeHkyZXA5QmEzZmpEcWNLVTNkbGsxTWpLZHY2RkNGSFkvb2dOOWtGS05iaHdLV0RURm1peUFjV0lpN1FMSU9YZE1raXFMQkgrVyt4aEdZUUE4RlRrU2tmMlVTbWtYK2YyMDJSazlBZDBwTjdwakppRjN0ZDFESmpiaDJkdkFSMFV4eWxRd1dmclJtRkFZaVBFR1VCSy9hUys4dUsrT2MyTURlTjJrWU9zT0pkNVV3YjBYUUdteUhwZ09WQnEraW5tNkF5ay9BaUd1NERsQlVuNHp2QVh4MW5zUFRCTXd2dmRmMlp6TjNWNE13PT0iIC8+PC9jZmRpOkNvbXBsZW1lbnRvPjwvY2ZkaTpDb21wcm9iYW50ZT4=",
            "pdf": "Base64 del PDF"
        },
        {
            "folio": "E7815AC7-7275-40AA-AD06-4C5B7D27EFA6",
            "rfcEmisor": "XXXX999999XXX",
            "razonSocialEmisor": "BBVA MEXICO, S.A., INSTITUCION DE BANCA MULTIPLE, GRUPO FINANCIERO BBVA MEXICO.",
            "rfcReceptor": "XXXX999999XXX",
            "razonSocialReceptor": "JUAN ALBERTO PEREZ GONZALEZ",
            "fechaEmision": "2022-06-01T02:41:08",
            "fechaCertificacion": "2022-06-01T07:58:18",
            "pac": "CEC961028A98",
            "monto": "$0.00",
            "efecto": "Ingreso",
            "estatus": "Cancelable sin aceptación",
            "estado": "Vigente",
            "estatusProcesoCancelacion": null,
            "fechaProcesoCancelacion": null,
            "rfcCuentaTerceros": null,
            "xml": "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz48Y2ZkaTpDb21wcm9iYW50ZSB4bWxuczp4c2k9Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1hLWluc3RhbmNlIiB4bWxuczp0ZmQ9Imh0dHA6Ly93d3cuc2F0LmdvYi5teC9UaW1icmVGaXNjYWxEaWdpdGFsIiB4c2k6c2NoZW1hTG9jYXRpb249Imh0dHA6Ly93d3cuc2F0LmdvYi5teC9jZmQvMyBodHRwOi8vd3d3LnNhdC5nb2IubXgvc2l0aW9faW50ZXJuZXQvY2ZkLzMvY2ZkdjMzLnhzZCIgVmVyc2lvbj0iMy4zIiBTZXJpZT0iQyIgRm9saW89IjMzMSIgRmVjaGE9IjIwMjItMDctMjlUMTI6NTI6NDYiIFNlbGxvPSJIM1BZbjJ2T0c0NHNtQkkwNE93UDVaNVhGRk0zblI1cmhackxGWlZwZnE4UVRLTEM1bkk3OTArZEF4dlplTVZjQitjRVQ3Sjd0clNaRWRXakE2SzVJenhSUkQwcTlVaU9yRDRuZUJ4aGJhZXRwK3V6WWxJRDJkWm5jL1RFU3liYzNGYUtIWmNmL0pnVWQwOVhMT2I1OFB4dVFXcHRGdVQyMjk1Y2dUU1dUa1BpN2JoZWFQOTl6OE1uTDM0TU1sdy9ZVmRuR090a29Dak5JT0h5dG9qMS95UEhkR2krRStiS1dLYnZ3ZDVOUU5tU2pXUUFMQm1CRHc4S213Q3RZMmgxNFA2T3dpdVl5Q3ZNZVg1U0VxQzZlZldjNG9EZklheS8xNWZLMHhLUExjVzR4b0E1WWFGK3NOTFRHMWZvZVNVZlUvNDVwM1lFdkF6cmF2bG9vUlFFblE9PSIgRm9ybWFQYWdvPSI5OSIgTm9DZXJ0aWZpY2Fkbz0iMDAwMDEwMDAwMDA1MDAzNTQzOTkiIENlcnRpZmljYWRvPSJNSUlHQkRDQ0EreWdBd0lCQWdJVU1EQXdNREV3TURBd01EQTFNREF6TlRRek9Ua3dEUVlKS29aSWh2Y05BUUVMQlFBd2dnR0VNU0F3SGdZRFZRUUREQmRCVlZSUFVrbEVRVVFnUTBWU1ZFbEdTVU5CUkU5U1FURXVNQ3dHQTFVRUNnd2xVMFZTVmtsRFNVOGdSRVVnUVVSTlNVNUpVMVJTUVVOSlQwNGdWRkpKUWxWVVFWSkpRVEVhTUJnR0ExVUVDd3dSVTBGVUxVbEZVeUJCZFhSb2IzSnBkSGt4S2pBb0Jna3Foa2lHOXcwQkNRRVdHMk52Ym5SaFkzUnZMblJsWTI1cFkyOUFjMkYwTG1kdllpNXRlREVtTUNRR0ExVUVDUXdkUVZZdUlFaEpSRUZNUjA4Z056Y3NJRU5QVEM0Z1IxVkZVbEpGVWs4eERqQU1CZ05WQkJFTUJUQTJNekF3TVFzd0NRWURWUVFHRXdKTldERVpNQmNHQTFVRUNBd1FRMGxWUkVGRUlFUkZJRTFGV0VsRFR6RVRNQkVHQTFVRUJ3d0tRMVZCVlVoVVJVMVBRekVWTUJNR0ExVUVMUk1NVTBGVU9UY3dOekF4VGs0ek1Wd3dXZ1lKS29aSWh2Y05BUWtDRTAxeVpYTndiMjV6WVdKc1pUb2dRVVJOU1U1SlUxUlNRVU5KVDA0Z1EwVk9WRkpCVENCRVJTQlRSVkpXU1VOSlQxTWdWRkpKUWxWVVFWSkpUMU1nUVV3Z1EwOU9WRkpKUWxWWlJVNVVSVEFlRncweE9UQTJNakF5TURFeE5USmFGdzB5TXpBMk1qQXlNREV4TlRKYU1JSFNNU1l3SkFZRFZRUURFeDFHU1U1QlRrOVdRU0JUUVZCSklFUkZJRU5XSUZOUFJrOU5JRVZPVWpFbU1DUUdBMVVFS1JNZFJrbE9RVTVQVmtFZ1UwRlFTU0JFUlNCRFZpQlRUMFpQVFNCRlRsSXhKakFrQmdOVkJBb1RIVVpKVGtGT1QxWkJJRk5CVUVrZ1JFVWdRMVlnVTA5R1QwMGdSVTVTTVNVd0l3WURWUVF0RXh4R1NVNHhOREE1TXpCSFVqWWdMeUJOUlZOV09EUXhNREExUlVjd01SNHdIQVlEVlFRRkV4VWdMeUJOUlZOV09EUXhNREExU0VOSVRsQkRNRFF4RVRBUEJnTlZCQXNUQ0VaSlRrRk9UMVpCTUlJQklqQU5CZ2txaGtpRzl3MEJBUUVGQUFPQ0FROEFNSUlCQ2dLQ0FRRUFpeHdHNTRBd3pZZ1NXdStHZnE3WGVRVUF2VStCMm16aUMzRHI5b1JJeisybzMwZkI5N3dRSEdxUlNkejlBTk9sdGJ2YkZyODRXcWJvT2pZN1pzRHVheVprS0VIbnVVMWxnZ2kzYjRQUkNya3R0RlhuOXFoL2lOQ1dFQUlORVY3NU9BaHM4WnlENDYwQk9NV3BSTVQ5RHdJOGYrRGVGNS9GV1ZCeXNRZkN2a0wvN3Z0OEF5UnZWYXpNTy9xNzJUYjMxczNkQWRHMy9sWkZGeWxFOUJ3UFB5RFRYY0FlTllKbUM0ODdVL1BTYjQzWmE1QUZRY0hQQ2V0eW52eU5vRTAreU4wZGUxSW1LeHJVVmR3T1huNzQveWhZdCt4R00vekdHejA3Y1o4eWdGV0ZpMFBRVFhnejIxbUY1dEtFNTZOaXJWU2ZwVUNHVzRXaDlwNmVwbU0yNVFJREFRQUJveDB3R3pBTUJnTlZIUk1CQWY4RUFqQUFNQXNHQTFVZER3UUVBd0lHd0RBTkJna3Foa2lHOXcwQkFRc0ZBQU9DQWdFQWt5cEJXcFdtR2tTbEI3N3VkSE5MWXNaRHlwMXZVMXJCOUQyY05QTzlVa0dGOTBlKzYwV04wVTBCWGZ3K1JIcVdqZG90SXhrOERXdXZRY2ZTWFE2UEVJOUNVVDdUNG9qay94ZWcvTzZDdTd2N3hoY2FoY1YrdzZvaHFFVXhVSUFYOUk0SUJpT1lGN0FmMjlONml5SU9yVTZ4WUx3UFFNTVRNZmZwREtYWVB3SWxRTlRYUFdYcGFSWVpTbzJmcWZyTjdSa0FSZHdRUzc1Ty9JMVE5d2pOQ05OYW5ZS1Q3K0dPT0dONjRjOE9jejhiVm9WNGxrbVpLYXhqU2VSOFRJVEVHS0RDR3F1V2s5RmozVWVqenBvYmpRMnExWlhYbnFrSWs0NThQcERUaWI0OTZoQVFiV0Nid2RPZnF5ZXNnSjBRNlp5a2FSalAxWm00OTNhL2J0K216ZS93WUFjMGxKKzBFUElGbkhIanJNZ053WW9FQ3krWGlvTjNmUHE0SHZZa0tZTDMxN29HTFpHUjU4WVcwM1pmdGI5c29HN1pEOTBadWhDbGg3TmEyTExmekhQU3BLZXMySXQ3SDdwdXZIbDgvdllqeUlLcWZCa056U0FBSU5QMWQrblBGSENjUkc1WldJM24zbmlnQmxDU1lRTjRCdDF6UEl3QnFheWdlZWVadm5LM3J0cldPb2gwbGZtaCs2TUM0Q0ovd1FTbW5QNFZBVHdmUXlqdE1vS2Z0aWpmTENQWHRDTzlxMmM0S3hpaXlHVGpyd0FDVjBjYWZqR1NFdVZVQjd4aGwxN0dKMFFUTlpjTGdvTkVIRG1GWTdPYVJwNVpLYm50ZTNCS3pRUTJWYk1jd3BLM3F5N09hYmZkcE9Lc1d2eWExeUNBdWxUNnFrNW9aYXJuMlQ4PSIgU3ViVG90YWw9Ijk4MC4yNyIgTW9uZWRhPSJNWE4iIFRvdGFsPSI5ODAuMjciIFRpcG9EZUNvbXByb2JhbnRlPSJJIiBNZXRvZG9QYWdvPSJQUEQiIEx1Z2FyRXhwZWRpY2lvbj0iMzExMTAiIHhtbG5zOmNmZGk9Imh0dHA6Ly93d3cuc2F0LmdvYi5teC9jZmQvMyI+PGNmZGk6RW1pc29yIFJmYz0iRklOMTQwOTMwR1I2IiBOb21icmU9IkZJTkFOT1ZBIFNBUEkgREUgQ1YgU09GT00gRU5SIiBSZWdpbWVuRmlzY2FsPSI2MDEiIC8+PGNmZGk6UmVjZXB0b3IgUmZjPSJUQ0ExNTAyMjRTWDUiIE5vbWJyZT0iRWwgMzAgQ2F0dGxlIFMuUC5SLiBkZSBSLkwuIGRlIEMuVi4iIFVzb0NGREk9IkcwMyIgLz48Y2ZkaTpDb25jZXB0b3M+PGNmZGk6Q29uY2VwdG8gQ2xhdmVQcm9kU2Vydj0iODQxMDE3MDMiIE5vSWRlbnRpZmljYWNpb249Ijg0MTAxNzAzIiBDYW50aWRhZD0iMSIgQ2xhdmVVbmlkYWQ9IkU0OCIgVW5pZGFkPSJFNDgiIERlc2NyaXBjaW9uPSJJbnRlcmVzZXMgZGV2ZW5nYWRvcyBkZWwgbWVzIGRlIEp1bGlvIGRlbCAyMDIyIDMwIENhdHRsZSA4OS1SRTEtMDEiIFZhbG9yVW5pdGFyaW89Ijk4MC4yNyIgSW1wb3J0ZT0iOTgwLjI3Ij48Y2ZkaTpJbXB1ZXN0b3M+PGNmZGk6VHJhc2xhZG9zPjxjZmRpOlRyYXNsYWRvIEJhc2U9Ijk4MC4yNyIgSW1wdWVzdG89IjAwMiIgVGlwb0ZhY3Rvcj0iVGFzYSIgVGFzYU9DdW90YT0iMC4wMDAwMDAiIEltcG9ydGU9IjAuMDAiIC8+PC9jZmRpOlRyYXNsYWRvcz48L2NmZGk6SW1wdWVzdG9zPjwvY2ZkaTpDb25jZXB0bz48L2NmZGk6Q29uY2VwdG9zPjxjZmRpOkltcHVlc3RvcyBUb3RhbEltcHVlc3Rvc1RyYXNsYWRhZG9zPSIwLjAwIj48Y2ZkaTpUcmFzbGFkb3M+PGNmZGk6VHJhc2xhZG8gSW1wdWVzdG89IjAwMiIgVGlwb0ZhY3Rvcj0iVGFzYSIgVGFzYU9DdW90YT0iMC4wMDAwMDAiIEltcG9ydGU9IjAuMDAiIC8+PC9jZmRpOlRyYXNsYWRvcz48L2NmZGk6SW1wdWVzdG9zPjxjZmRpOkNvbXBsZW1lbnRvPjx0ZmQ6VGltYnJlRmlzY2FsRGlnaXRhbCB4c2k6c2NoZW1hTG9jYXRpb249Imh0dHA6Ly93d3cuc2F0LmdvYi5teC9UaW1icmVGaXNjYWxEaWdpdGFsIGh0dHA6Ly93d3cuc2F0LmdvYi5teC9zaXRpb19pbnRlcm5ldC9jZmQvVGltYnJlRmlzY2FsRGlnaXRhbC9UaW1icmVGaXNjYWxEaWdpdGFsdjExLnhzZCIgVmVyc2lvbj0iMS4xIiBVVUlEPSIyMjAzYzRlMi02ZjM3LTQ0MzMtYWVkMC1mNjM3NmVjNjM3MzEiIEZlY2hhVGltYnJhZG89IjIwMjItMDctMjlUMTM6NTI6NDYiIFJmY1Byb3ZDZXJ0aWY9IkxTTzEzMDYxODlSNSIgU2VsbG9DRkQ9IkgzUFluMnZPRzQ0c21CSTA0T3dQNVo1WEZGTTNuUjVyaFpyTEZaVnBmcThRVEtMQzVuSTc5MCtkQXh2WmVNVmNCK2NFVDdKN3RyU1pFZFdqQTZLNUl6eFJSRDBxOVVpT3JENG5lQnhoYmFldHArdXpZbElEMmRabmMvVEVTeWJjM0ZhS0haY2YvSmdVZDA5WExPYjU4UHh1UVdwdEZ1VDIyOTVjZ1RTV1RrUGk3YmhlYVA5OXo4TW5MMzRNTWx3L1lWZG5HT3Rrb0NqTklPSHl0b2oxL3lQSGRHaStFK2JLV0tidndkNU5RTm1TaldRQUxCbUJEdzhLbXdDdFkyaDE0UDZPd2l1WXlDdk1lWDVTRXFDNmVmV2M0b0RmSWF5LzE1ZksweEtQTGNXNHhvQTVZYUYrc05MVEcxZm9lU1VmVS80NXAzWUV2QXpyYXZsb29SUUVuUT09IiBOb0NlcnRpZmljYWRvU0FUPSIwMDAwMTAwMDAwMDUwOTg0NjY2MyIgU2VsbG9TQVQ9IkRzRGk0TzVWamMrTWVjWmJBdVhsMU53QlZQV21TL0J3UEM5eGM2aUJGQmhnUE9abFF2NGF4WlJjR0p3QmRldFNMRWVuMU40SVRFaXBlcGI3Q1lPWkpvRE03c3pIb3FNTXJNcEpsdTNBc1dvTzkzWWNIMW8yQ2twZDVmYXlkMzhiQ0RXNlNPa1FiMHY1aHplZWlPQ0JRRUllRzZxejIwZnAwbTlkbkoxVyswUzFaMFpleUY1bzZoZlNyV3M4Qkt5TVJzNHhXVHp5ZVJYOFF6YWl1SDRURUgydmV5RTZuZkR6cys1ck9nRHpvcjh5SzlMaENPQ2hSSFQ3RUFHZFBJUGNXT3oyclFLNElnOGVOSzJSL1Fzc3lMKytnM0VpT3VsWlQyRHY2cExWZC9LSE5LeC96Q1JOdVdxYmRzQjh1dHZ3L2h4TFozRkFsWlpRbjZ3S0tSck9Jdz09IiAvPjwvY2ZkaTpDb21wbGVtZW50bz48L2NmZGk6Q29tcHJvYmFudGU+",
            "pdf": "Base64 del PDF"
        }
    ],
    "estatus": "OK",
    "claveMensaje": 0,
    "codigoValidacion": "gf1657073270.0487676"
}'''


def json_to_python(json_string):
    """
    Convierte un String de JSON a Python.
    Su único parámetro acepta un String que contenga los datos de Nubarium
    de "Get invoices from SAT with CIEC".
    """
    json_text = json.loads(json_string)
    nc = get_nombre_cliente(json_text)
    return json_text, nc


def get_nombre_cliente(json_text):
    try:
        nombre_cliente = json_text['facturasEmitidas'][0]['razonSocialEmisor']
    except KeyError:
        nombre_cliente = json_text['facturasRecibidas'][0]['razonSocialReceptor']
    return nombre_cliente


# Resumen del JSON de Nubarium
# def get_summary(text):
#     """
#     Devuelve en 3 variables de tipo Decimal el total de las facturas en forma
#     de un diccionario, ejemplo:
#
#     dict_resumen = {
#         'totalEmitidas': Total de facturación emitida en el mes,
#         'totalRecibidas': Total de facturación recibida en el mes,
#         'totalDiferencia': Total de la diferencia (emitida - recibida)
#     }
#
#     Decimal permite precisión mejorada para valores monetarios.
#     Del JSON se obtienen los datos en Strings, se eliminan los '$' y las comas.
#     """
#     total_emitidas = Decimal((text['totalEmitidas']).replace('$', '').replace(',', ''))
#     total_recibidas = Decimal((text['totalRecibidas']).replace('$', '').replace(',', ''))
#     total_diferencia = Decimal((text['totalDiferencia']).replace('$', '').replace(',', ''))
#     dict_resumen = {
#         'totalEmitidas': total_emitidas,
#         'totalRecibidas': total_recibidas,
#         'totalDiferencia': total_diferencia
#     }
#     return dict_resumen


def main():
    json_to_python(string_prueba)


if __name__ == '__main__':
    main()
