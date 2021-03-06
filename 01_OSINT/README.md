# OSINT

- [OSINT](#osint)
  - [External Resource](#external-resource)
  - [Book](#book)
  - [Chalenges](#chalenges)
  - [Local IP](#local-ip)
  - [VMs](#vms)
  - [Search Engines](#search-engines)
  - [Google Dorks](#google-dorks)
    - [Operators](#operators)
  - [Dorks](#dorks)
  - [Video Search Engines](#video-search-engines)
  - [Image Search Engines](#image-search-engines)
    - [Image Tools](#image-tools)
  - [Geolocation Recon](#geolocation-recon)
    - [Satelite](#satelite)
    - [3 word location](#3-word-location)
  - [Google Alerts](#google-alerts)
  - [PT](#pt)
  - [Find people](#find-people)
  - [Social Networking Recon](#social-networking-recon)
    - [Social Media](#social-media)
    - [Security questions](#security-questions)
    - [Facebook](#facebook)
    - [Twitter](#twitter)
    - [Instagram](#instagram)
  - [Username OSINT](#username-osint)
  - [Personal Information](#personal-information)
  - [Bitcoin](#bitcoin)
  - [Job Board Recon](#job-board-recon)
  - [Search Code](#search-code)
  - [Deep/Dark Web Recon](#deepdark-web-recon)
    - [Access](#access)
    - [Sites](#sites)
    - [Onion sites](#onion-sites)
  - [Metadata Recon](#metadata-recon)
  - [Email Tracking](#email-tracking)
  - [Website Information](#website-information)
  - [Public Network Footprinting](#public-network-footprinting)
    - [Network Range](#network-range)
    - [Autonomous System Numbers](#autonomous-system-numbers)
    - [WHOIS and DNS](#whois-and-dns)
    - [DNS Zone Transfer](#dns-zone-transfer)
    - [Reverse DNS Lookup](#reverse-dns-lookup)
    - [Traceroute](#traceroute)
    - [Sub-Domain Enumeration](#sub-domain-enumeration)
    - [Recon-ng](#recon-ng)
    - [Maltego](#maltego)
  - [Other Footprinting Tools](#other-footprinting-tools)
  - [Wifi](#wifi)
  - [WaybackMachine](#waybackmachine)
  - [Canary Tokens](#canary-tokens)
  - [Tools](#tools)
  - [Shodan, Censys, and Thingful](#shodan-censys-and-thingful)
    - [Shodan Guide](#shodan-guide)
      - [Shodan Dorks](#shodan-dorks)
  - [Website cloner](#website-cloner)
  - [Password OSINT](#password-osint)
  - [Temporary Email](#temporary-email)
  - [VPN](#vpn)
  - [DNS Leak](#dns-leak)
  - [Sock Puppets](#sock-puppets)
    - [Sock Puppets Tutorials](#sock-puppets-tutorials)
  - [Scams](#scams)
  - [Browser OSINT](#browser-osint)

---

## External Resource

- <https://osintframework.com/>
- <https://www.osintdojo.com/resources/>
- <https://www.youtube.com/channel/UChbp7r-Lezl1CBNQWBDYGeQ>
- <https://osintcurio.us/>
- <https://github.com/jivoi/awesome-osint>
- <https://i-intelligence.eu/uploads/public-documents/OSINT_Handbook_2020.pdf>
- <https://github.com/TCM-Course-Resources/Open-Source-Intellingence-Resources>
- <https://www.youtube.com/watch?v=z6ghArAWwWc>
- IntelligenceX - <https://intelx.io/>

---

## Book

- OSINT Handbook 2020 - [link](OSINT_Handbook_2020.pdf)

---

## Chalenges

- <https://investigator.cybersoc.wales/>
- <https://ctf.cybersoc.wales/>

---

## Local IP

- `http://ipinfo.io/ip`

---

## VMs

- Tracelabs OSINT VM - <https://www.tracelabs.org/initiatives/osint-vm>
- TraceLabs OSINT VM Installation Guide - <https://download.tracelabs.org/Trace-Labs-OSINT-VM-Installation-Guide-v2.pdf>
- ThreatPursuit-VM - <https://github.com/mandiant/ThreatPursuit-VM>
- REMnux - <https://docs.remnux.org/install-distro/get-virtual-appliance>
- Genymotion - <https://www.genymotion.com/download/>

---

## Search Engines

- Google - <https://www.google.com>
- Bing - <https://www.bing.com>
- Yahoo - <https://www.yahoo.com>
- Ask - <https://www.ask.com/>
- Aol - <https://www.aol.com>
- Baidu - <https://www.baidu.com/>
- WolframAlpha - <https://www.wolframalpha.com/>
- DuckDuckGo - <https://duckduckgo.com/>
- Yandex - <https://yandex.com/>

---

## Google Dorks

- Google Advanced Search <https://www.google.com/advanced_search>
- Google Hacking Database - <https://www.exploit-db.com/google-hacking-database>
- gbhackers - <https://gbhackers.com/latest-google-dorks-list/>
- google-dork-list - <https://www.boxpiper.com/posts/google-dork-list>
- Google Guide - <http://www.googleguide.com/using_advanced_operators.html> - <http://www.googleguide.com/print/adv_op_ref.pdf>

### Operators

- **filetype:** search your results based on the file extension
- **cache:** This operator allows you to view cached version of the web page.
- **allinurl:** This operator restricts results to pages containing all the query terms specified in the URL.
- **inurl:** This operator restricts the results to pages containing the word specified in the URL
- **allintitle:** This operator restricts results to pages containing all the query terms specified in the title.
- **inanchor:** This operator restricts results to pages containing the query terms specified in the anchor text on links to the page.
- **allinanchor:** This operator restricts results to pages containing all query terms specified in the anchor text on links to the page.
- **link:** This operator searches websites or pages that contain links to the specified website or page.
- **related:** This operator displays websites that are similar or related to the URL specified.
- **info:** This operator finds information for the specified web page.
- **location:** This operator finds information for a specific location.

- 42 Advanced Operators - <https://ahrefs.com/blog/google-advanced-search-operators/>

---

## Dorks

- `recibo vencimento ext:pdf`
- `indexof site:pt`
- `inurl:admin site:pt`
- `password`
- `hackedby`

---

## Video Search Engines

- YouTube - <https://www.youtube.com/>
- YouTube DataViewer - <https://citizenevidence.amnestyusa.org/>
- Google Videos - <https://www.google.com/videohp>
- Yahoo Video Search - <https://video.search.yahoo.com>
- Video Reverse - <https://www.videoreverser.com/>

---

## Image Search Engines

- Google Images - <https://images.google.com/>
- Yahoo Images - <https://images.search.yahoo.com/>
- Yandex Images - <https://yandex.com/images/>
- Image Reverse - TinEye - <https://tineye.com/>
- Image Reverse - ezgif - <https://ezgif.com/reverse>
- Pimeyes - <https://pimeyes.com/en>

### Image Tools

- Remove Background - <https://www.remove.bg/>
- Cleanup Pictures - <https://cleanup.pictures>

---

## Geolocation Recon

- Google Maps - <https://www.google.com/maps>
- Bing Maps - <https://www.bing.com/maps/>
- Wikimapia - <https://wikimapia.org>
- Tips, Tricks and Techniques - <https://somerandomstuff1.wordpress.com/2019/02/08/geoguessr-the-top-tips-tricks-and-techniques/>

### Satelite

- World Imagery - <https://livingatlas.arcgis.com/>
- World Imagery Wayback - <https://livingatlas.arcgis.com/wayback/>

### 3 word location

- what3words - <https://what3words.com/>

---

## Google Alerts

- Google Alerts - <https://www.google.com/alerts>

---

## PT

- Contracts - <https://www.base.gov.pt>
- Search DRE - <https://dre.tretas.org>
- Penhorados - <https://www.pesquisabenspenhorados.com/leiloes-vendas-financas/default.aspx>
- Automovel - Pedido da Certid??o Permanente do Registo Autom??vel dos Registos em Vigor - <https://www.automovelonline.mj.pt/AutoOnlineProd/FrontOfficeController?action=validaMatricula&url=FrontOfficeController%3Faction%3Dpedidocertidao&contr=FrontOfficeController>
- VIN Search - <https://www.lastvin.com/>
- Predial - <https://www.predialonline.pt/>
- DGES - <https://www.dges.gov.pt>
- Seguro - <https://www.asf.com.pt/isp/Templates/Atendimento/PesquisaVeiculoSeguro.aspx?FRAMELESS=false&NRNODEGUID=%7b09089E16-115D-4C82-9C64-FDA43D5FF098%7d&NRORIGINALURL=%2fNR%2fexeres%2f019EEB91-E357-4A7C-8BD2-B62293701692%2ehtm&NRCACHEHINT=Guest>

---

## Find people

- Hunter - <https://hunter.io>
- Phonebook.cz - <https://phonebook.cz/>
- VoilaNorbert - <https://www.voilanorbert.com/>
- Clearbit Connect - <https://connect.clearbit.com/>
- Email Hippo - <https://tools.emailhippo.com/>
- Email Checker - <https://email-checker.net/>

---

## Social Networking Recon

- **theHarvester** - <https://github.com/laramies/theHarvester>
  - `theHarvester -d microsoft.com -l 200 -b baidu`
  - `theHarvester -d eccouncil -l 200 -b linkedin`
  - `theHarvester -f theHarvester_results.xml -b 'baidu,bing,duckduckgo,google,yahoo,netcraft,linkedin,twitter' -l 500 -d somedomain.com`
- Sherlock - <https://github.com/sherlock-project/sherlock>
  - `python3 sherlock satya nadella`
- Social Searcher - <https://www.social-searcher.com/>
- UserRecon - <https://github.com/issamelferkh/userrecon>
  - `./userrecon.sh`

---

### Social Media

- Friends and followers
- Media (pictures, videos, audio)
- Posts/Comments
- Phone numbers/ Dates / Schedules
- Likes / Dislikes

---

### Security questions

- What was your childhood nickname?
- What is the first school you attended?
- What was your first pets name?
- What street did you grow up on?
- What's the ciry where your parents met?
- What was the city you where born in?
- What's the name of your oldest cousin?

---

### Facebook

- StalkFace - <https://stalkface.com/en/>
- Sowdust Github - <https://www.sowsearch.info/>
- IntelligenceX Facebook Search - <https://intelx.io/tools?tab=facebook>

---

### Twitter

- Twitter Advanced Search - <https://twitter.com/search-advanced>
- Twint - <https://github.com/twintproject/twint>
- Botometer - <https://botometer.osome.iu.edu/>

---

### Instagram

- Instaloot - <https://github.com/althonos/InstaLooter>

---

## Username OSINT

- NameChk - <https://namechk.com/>
- WhatsMyName - <https://whatsmyname.app/>
- NameCheckup - <https://namecheckup.com/>

## Personal Information

- Social Bearing - <https://socialbearing.com/>
- Peek You - <https://www.peekyou.com/>
- Pipl - <https://pipl.com/>
- KnowEM - <https://knowem.com/>
- Intelius - <https://www.intelius.com/>
- Sync me - <https://sync.me/>
- True Caller - <https://www.truecaller.com/>

---

## Bitcoin

- Bitcoin Whos Who - <https://www.bitcoinwhoswho.com/>
- Bit Ref - <https://bitref.com>

---

## Job Board Recon

- Monster - <https://www.monster.com/>
- Smart Recruiters - <https://www.smartr.me/>
- Linkedin - <https://www.linkedin.com/>
- Xing - <https://www.xing.com/>
- Glassdoor - <https://www.glassdoor.com/>

---

## Search Code

- Search code - <https://searchcode.com/>

---

## Deep/Dark Web Recon

- Dark Nets
  - Friend-2-Friend
    - Very anonymous Peer-2-Peer network
      - <https://freenetproject.org>
      - <https://retroshare.cc/>
  - Privacy Networks
    - Tor

### Access

- Tor - <https://www.torproject.org/>
  - Check if Ip is Tor - ExoneraTor - <https://metrics.torproject.org/exonerator.html>
- **Tails** - <https://tails.boum.org/>
- Whonix - <https://www.whonix.org/>
&nbsp;&nbsp;

### Sites

- <https://iaca-darkweb-tools.com/>
- <https://onionsearchengine.com/>
- <https://thehiddenwiki.org>

### Onion sites

- The Hidden Wiki - <http://zqktlwi4fecvo6ri.onion/wiki/index.php/Main_Page> is an onion site that works as a Wikipedia service of hidden websites
- FakeID - <http://fakeidskhfik46ux.onion> is an onion site for creating fake passports
- The Paypal Cent - <http://nare7pqnmnojs2pg.onion> is an onion site that sells PayPal accounts with good balances

---

## Metadata Recon

- strings
  - `strings file`
- On-line - <http://exif.regex.info/exif.cgi>
- exif - sudo apt install exif
  - `exif file`
- metagoofil - <https://github.com/opsdisk/metagoofil> - <https://github.com/laramies/metagoofil>
  - `metagoofil -d certifiedhacker.com -t pdf,doc,xls,ppt,txt -e 200`
  - `metagoofil -o metagoofil_results -u 'Randomize User-Agent' -r 10 -e 45 -l 100 -n 100 -w -t 'pdf,doc,docx,xls,xlsx' -d somedomain.com`
- exiftool - <https://exiftool.org/>
  - `exiftool file`

---

## Email Tracking

- Infoga - <https://github.com/m4ll0k/Infoga>
- EmailTrackerPro - <http://www.emailtrackerpro.com/>
- bitly - <https://bitly.com/>
- Linkly - <https://linklyhq.com/>

---

## Website Information

- robots.txt
- sitemap.xml
- viewsource
- Measure page quality - <https://web.dev/measure/>
- seo-analyzer - <https://neilpatel.com/seo-analyzer/>
- whatweb - <https://morningstarsecurity.com/research/whatweb>
- wappalyzer - <https://www.wappalyzer.com/>
- Builtwith - <https://builtwith.com/>
- Website Informer - <https://website.informer.com/>
- Web Data Extractor - <http://www.webextractor.com/>

---

## Public Network Footprinting

- <https://mxtoolbox.com>
- <https://dnschecker.org/all-dns-records-of-domain.php>
- <https://dnsspy.io/scan/>
- <https://centralops.net/co/DomainDossier.aspx>

### Network Range

- IANA (Internet Assigned Numbers Authority) - <https://www.iana.org/numbers>
- ARIN  (American Registry for Internet Numbers) - <https://www.arin.net/about/welcome/region/>
- RIPE  () - <https://www.ripe.net/>

---

### Autonomous System Numbers

- IP address into an ASN - <https://www.ultratools.com/tools/asnInfo>

---

### WHOIS and DNS

- **Domain Tools Whois** - <https://whois.domaintools.com/>
- Network Tools - <https://network-tools.com/>
- DNS Stuff - <https://www.dnsstuff.com/freetools>
- Batch IP Converter - <http://www.sabsoft.com/BatchIPConverter.htm>
&nbsp;&nbsp;
- nslookup
  - `nslookup certifiedhacker.com`
    - interactive: set type=a
    - cname: set type=cname
- dmtry
  - `dmitry -i www.certifiedhacker.com`
- dig
  - `dig certifiedhacker.com`
  - `dig yahoo.com mx`
  - `dig yahoo.com SOA`
  - `dig yahoo.com ANY +noall +answer`
- dnsrecon
  - `dnsrecon -d certifiedhacker.com`
- nslookup - <http://www.kloth.net/services/nslookup.php>

---

### DNS Zone Transfer

- dig
  - `dig axfr @nsztm1.digi.ninja zonetransfer.me`
- digi.ninja - <https://digi.ninja/projects/zonetransferme.php>

---

### Reverse DNS Lookup

- Network Tools - <https://www.yougetsignal.com/>
- dnsrecon - <https://github.com/darkoperator/dnsrecon>
  - `dnsrecon -r 162.241.216.0/24`

---

### Traceroute

- Traceroute
  - `traceroute www.certifiedhacker.com`
  - ICMP
    - `traceroute -I`
  - TCP
    - `traceroute -T`
- tcptraceroute
  - `tcptraceroute`
&nbsp;&nbsp;
- Path Analyzer Pro - <https://www.pathanalyzer.com>
- VisualRoute  - <https://www.visualroute.com>

---

### Sub-Domain Enumeration

- Domains - gTLD (Generic Top-Level Domain)
- Sub-Domains
&nbsp;&nbsp;
- Google - <https://www.google.com>
  - `site:itpro.tv`
- Netcraft Tools - <https://www.netcraft.com/tools/>
- **Netcraft Site Report** - <https://sitereport.netcraft.com/?url=https://www.eccouncil.org/>
- **Netcraft Search DNS** - <https://searchdns.netcraft.com/?host=*.eccouncil.org>
- sublist3r - <https://github.com/aboul3la/Sublist3r>
  - `python3  ./sublist3r.py -d domain.com -o domain.com.txt`
- httprobe - <https://github.com/tomnomnom/httprobe>
- **Amass** - <https://github.com/OWASP/Amass>

- crt.sh - <https://crt.sh/>
- **DNS Dumpster** - <https://dnsdumpster.com/>
- **Hacker Target** - <https://hackertarget.com>
- **ipinfo.io** - <https://ipinfo.io>
- Pentest Tools - <https://pentest-tools.com/>

**More Info** - <https://hover.blog/whats-a-domain-name-subdomain-top-level-domain/>

---

### Recon-ng

- **Recon-ng** - <https://github.com/lanmaster53/recon-ng>

---

### Maltego

- Maltego - <https://www.maltego.com/ce-registration/>

---

## Other Footprinting Tools

- Foca - <https://www.elevenpaths.com/innovation-labs/technologies/foca>
- OSINT Framework - <https://osintframework.com/>
- Recon-Dog - <https://github.com/s0md3v/ReconDog>
- Maltego - <https://www.maltego.com/>
- BillCipher - <https://github.com/84KaliPleXon3/BillCipher>
- OSRFramework - <https://github.com/i3visio/osrframework>
- Th3inspector - <https://github.com/Moham3dRiahi/Th3inspector>
- Raccoon - <https://github.com/evyatarmeged/Raccoon>
- orb - <https://github.com/epsylon/orb>
- spiderfoot - <https://github.com/smicallef/spiderfoot>

---

## Wifi

- wigle.net - <https://wigle.net>

---

## WaybackMachine

- WaybackMachine - <https://archive.org/web/>
- Archive.is - <http://archive.is/>
- Cached Pages - <http://www.cachedpages.com/>
- Cached View - <http://cachedview.com/>
- OldWeb.Today - <https://oldweb.today/>
- Time Travel - <http://timetravel.mementoweb.org/>

---

## Canary Tokens

- Canary Tokens - <https://canarytokens.org/generate>

---

## Tools

---

## Shodan, Censys, and Thingful

- Shodan - <https://help.shodan.io/the-basics/what-is-shodan>
- Censys - <https://about.censys.io/>
- Thingfull - <https://www.thingful.net/site/about>

### Shodan Guide

[Shodan](shodan.md)

#### Shodan Dorks

- `Remote desktop country:pt city:"Braga"`
- `winrest port:5901 country:pt`
- `smb contabilidade country:pt`
- `smb series country:pt`

---

## Website cloner

- wget
  - `wget -mkEpnp site`
- HTTrack Website Copier - <https://www.httrack.com/>

---

## Password OSINT

- HaveIBeenPwned - <https://haveibeenpwned.com/>
- Breach-Parse - <https://github.com/hmaverickadams/breach-parse>
- Dehashed - <https://dehashed.com/>
- WeLeakInfo - <https://weleakinfo.to/v2/>
- LeakCheck - <https://leakcheck.io/>
- SnusBase - <https://snusbase.com/>
- Scylla.so - <https://scylla.so/>

---

## Temporary Email

- 10 minute email - <https://10minutemail.com/>
- 20 minute email - <https://www.20minutemail.com/>

---

## VPN

- ProtonVPN - <https://protonvpn.com/>

---

## DNS Leak

- DNS Leak Test - <https://dnsleaktest.com/>

---

## Sock Puppets

- Fake Identity - <https://datafakegenerator.com/>
- Fake Identity - <https://www.fakenamegenerator.com/>
- Fake Photo - <https://thispersondoesnotexist.com/>
- Geolocation extensions - <https://chrome.google.com/webstore/category/extensions>
- Privacy.com - <https://privacy.com/join/LADFC>

### Sock Puppets Tutorials

- Intro to Creating an Effective Sock Puppet (wayback archive): <https://web.archive.org/web/20210307173507/https://jakecreps.com/sock-puppets/>
- The Art Of The Sock - <https://www.secjuice.com/the-art-of-the-sock-osint-humint/>
- My Process for Setting up Anonymous Sock Puppet Accounts - <https://garrettmickley.com/sockpuppet-account-creation/>

## Scams

- Scam Digger -  <https://scamdigger.com>

## Browser OSINT

- <https://webbrowsertools.com/>
- <https://browserleaks.com/>
