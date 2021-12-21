# OSINT

- [OSINT](#osint)
  - [External Resource](#external-resource)
  - [Local IP](#local-ip)
  - [VMs](#vms)
  - [Search Engines](#search-engines)
  - [Google Dorks](#google-dorks)
    - [Operators](#operators)
  - [Dorks](#dorks)
  - [Video Search Engines](#video-search-engines)
  - [Image Search Engines](#image-search-engines)
  - [Geolocation Recon](#geolocation-recon)
    - [3 word location](#3-word-location)
  - [Google Alerts](#google-alerts)
  - [Social Networking Recon](#social-networking-recon)
    - [Social Media](#social-media)
    - [Security questions](#security-questions)
    - [Facebook](#facebook)
    - [Twitter](#twitter)
    - [Instagram](#instagram)
  - [Personal Information](#personal-information)
  - [Job Board Recon](#job-board-recon)
  - [Deep/Dark Web Recon](#deepdark-web-recon)
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
    - [Shodan](#shodan)
      - [Shodan Dorks](#shodan-dorks)
  - [Website cloner](#website-cloner)
  - [Have I been Pwned](#have-i-been-pwned)
  - [Temporary Email](#temporary-email)
  - [VPN](#vpn)
  - [DNS Leak](#dns-leak)
  - [Dial Tone](#dial-tone)
  - [Chalenges](#chalenges)

---

## External Resource

- <https://osintframework.com/>
- <https://www.osintdojo.com/resources/>
- <https://www.youtube.com/channel/UChbp7r-Lezl1CBNQWBDYGeQ>

---

## Local IP

- `http://ipinfo.io/ip`

---

## VMs

- [OSINT VM] - <https://www.tracelabs.org/initiatives/osint-vm>
- [Buscador] - <https://inteltechniques.com/buscador/>
- [REMnux] - <https://docs.remnux.org/install-distro/get-virtual-appliance>
- [Genymotion] - <https://www.genymotion.com/download/>

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

- Google Hacking Database - <https://www.exploit-db.com/google-hacking-database>
- gbhackers - <https://gbhackers.com/latest-google-dorks-list/>
- google-dork-list - <https://www.boxpiper.com/posts/google-dork-list>
- Google Guide - <http://www.googleguide.com/using_advanced_operators.html>

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

---

## Geolocation Recon

- Google Maps - <https://www.google.com/maps>
- Bing Maps - <https://www.bing.com/maps/>
- Wikimapia - <https://wikimapia.org>

### 3 word location

- what3words - <https://what3words.com/>

---

## Google Alerts

- Google Alerts - <https://www.google.com/alerts>

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

### Social Media

- Friends and followers
- Media (pictures, videos, audio)
- Posts/Comments
- Phone numbers/ Dates / Schedules
- Likes / Dislikes

### Security questions

- What was your childhood nickname?
- What is the first school you attended?
- What was your first pets name?
- What street did you grow up on?
- What's the ciry where your parents met?
- What was the city you where born in?
- What's the name of your oldest cousin?

### Facebook

- StalkFace - <https://stalkface.com/en/>

### Twitter

- Twint - <https://github.com/twintproject/twint>

### Instagram

- Instaloot - <https://github.com/althonos/InstaLooter>

---

## Personal Information

- Peek You - <https://www.peekyou.com/>
- pipl - <https://pipl.com/>
- Intelius - <https://www.intelius.com/>
- Sync me - <https://sync.me/>

---

## Job Board Recon

- Monster - <https://www.monster.com/>
- Smart Recruiters - <https://www.smartr.me/>
- Linkedin - <https://www.linkedin.com/>
- Xing - <https://www.xing.com/>
- Glassdoor - <https://www.glassdoor.com/>

---

## Deep/Dark Web Recon

- Dark Nets
  - Friend-2-Friend
    - Very anonymous Peer-2-Peer network
      - <https://freenetproject.org>
      - <https://retroshare.cc/>
  - Privacy Networks
    - Tor
&nbsp;&nbsp;
- Tor - <https://www.torproject.org/>
  - Check if Ip is Tor - ExoneraTor - <https://metrics.torproject.org/exonerator.html>
- **Tails** - <https://tails.boum.org/>
- Whonix - <https://www.whonix.org/>
&nbsp;&nbsp;
- The Hidden Wiki - <http://zqktlwi4fecvo6ri.onion/wiki/index.php/Main_Page> is an onion site that works as a Wikipedia service of hidden websites
- FakeID - <http://fakeidskhfik46ux.onion> is an onion site for creating fake passports
- The Paypal Cent - <http://nare7pqnmnojs2pg.onion> is an onion site that sells PayPal accounts with good balances

## Metadata Recon

- strings
  - `strings file`
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
- [Measure page quality](https://web.dev/measure/)
- [seo-analyzer](https://neilpatel.com/seo-analyzer/)
- [whatweb](https://morningstarsecurity.com/research/whatweb)
- [wappalyzer](https://www.wappalyzer.com/)
- [Website Informer] - <https://website.informer.com/>
- [Web Data Extractor] - <http://www.webextractor.com/>

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
- Pentest Tools - <https://pentest-tools.com/>

**More Info** - <https://hover.blog/whats-a-domain-name-subdomain-top-level-domain/>

---

### Recon-ng

- **Recon-ng** - <https://github.com/lanmaster53/recon-ng>

---

### Maltego

- [Maltego] - <https://www.maltego.com/ce-registration/>

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

[wigle.net](wigle.net)

---

## WaybackMachine

[WaybackMachine](https://archive.org/web/)
[Archive.is](http://archive.is/)
[Cached Pages](http://www.cachedpages.com/)
[Cached View](http://cachedview.com/)
[OldWeb.Today](https://oldweb.today/)
[Time Travel](http://timetravel.mementoweb.org/)

---

## Canary Tokens

- [Canary Tokens] - <https://canarytokens.org/generate>

---

## Tools

---

## Shodan, Censys, and Thingful

- [Shodan] - <https://help.shodan.io/the-basics/what-is-shodan>
- [Censys] - <https://about.censys.io/>
- [Thingfull] - <https://www.thingful.net/site/about>

### Shodan

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
- [HTTrack Website Copier] - <https://www.httrack.com/>

---

## Have I been Pwned

- [haveibeenpwned] - <https://haveibeenpwned.com/>

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

## Dial Tone

- [Detect DTMF Tones] - <http://dialabc.com/sound/detect/>

---

## Chalenges

- <https://investigator.cybersoc.wales/>
- <https://ctf.cybersoc.wales/>

