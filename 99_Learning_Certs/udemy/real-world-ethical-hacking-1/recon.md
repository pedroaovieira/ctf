# Recon

## OSINT Framework

{% embed url="https://osintframework.com/" %}

## Domain Dossier

{% embed url="http://centralops.net/co/DomainDossier.aspx" %}

## theHarvester

![](../../.gitbook/assets/image.png)

```text
theHarvester -d ung.edu -b all -f report.html

theHarvester -d ung.edu -b linkedin,google -f report.html
```

## Recon-ng

![](../../.gitbook/assets/image%20%282%29.png)

```text
recon-ng

marketplace install recon

marketplace search hackertarget
modules load recon/domains-hosts/hackertarget
options list
options set SOURCE ung.edu
run
show hosts
```

## nmap

```text
nmap 10.0.9.9 -sV
```

## Legion \(Sparta\)

![](../../.gitbook/assets/image%20%283%29.png)









