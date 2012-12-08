%define pkgname dejavu-fonts-ttf

Summary: DejaVu ttf Fonts
Name: fonts-ttf-dejavu
Version: 2.33
Release: %mkrel 5
License: Bitstream Vera Fonts Copyright
Group: System/Fonts/True type
URL: http://dejavu.sourceforge.net/
Source0: http://prdownloads.sourceforge.net/dejavu/%{pkgname}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
BuildRequires: fontconfig
BuildRequires: freetype-tools

%description
The DejaVu fonts are modifications of the Bitstream Vera fonts designed 
to extend this original for greater coverage of Unicode. The Bitstream Vera 
family was limited mainly to the characters in the Basic Latin and Latin-1 
Supplement portions of Unicode (roughly equivalent to ISO-8859-15) but was 
released with a license that permitted changes. The DejaVu fonts project was 
started with the aim to "provide a wider range of characters... while 
maintaining the original look and feel through the process of collaborative 
development".

%prep
%setup -q -n %{pkgname}-%{version}

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_datadir}/fonts/TTF/dejavu

install -m 644 ttf/*.ttf %{buildroot}%{_datadir}/fonts/TTF/dejavu
ttmkfdir %{buildroot}%{_datadir}/fonts/TTF/dejavu > %{buildroot}%{_datadir}/fonts/TTF/dejavu/fonts.dir
ln -s fonts.dir %{buildroot}%{_datadir}/fonts/TTF/dejavu/fonts.scale

mkdir -p %{buildroot}%{_sysconfdir}/X11/fontpath.d/
ln -s ../../..%{_datadir}/fonts/TTF/dejavu \
	%{buildroot}%{_sysconfdir}/X11/fontpath.d/ttf-dejavu:pri=50
%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README LICENSE AUTHORS NEWS BUGS *cover.txt
%dir %{_datadir}/fonts/TTF/dejavu
%{_datadir}/fonts/TTF/dejavu/*.ttf
%verify(not mtime) %{_datadir}/fonts/TTF/dejavu/fonts.dir
%{_datadir}/fonts/TTF/dejavu/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-dejavu:pri=50


%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 2.33-3mdv2011.0
+ Revision: 675413
- br fontconfig for fc-query used in new rpm-setup-build

* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 2.33-2
+ Revision: 675177
- rebuild for new rpm-setup

* Thu Apr 21 2011 Sandro Cazzaniga <kharec@mandriva.org> 2.33-1
+ Revision: 656570
- new version

* Tue Aug 03 2010 Ahmad Samir <ahmadsamir@mandriva.org> 2.31-1mdv2011.0
+ Revision: 565190
- update to 2.31

* Wed Jan 20 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 2.30-2mdv2010.1
+ Revision: 494134
- fc-cache is now called by an rpm filetrigger

* Sat Aug 29 2009 Frederik Himpe <fhimpe@mandriva.org> 2.30-1mdv2010.0
+ Revision: 422268
- update to new version 2.30

* Wed Mar 11 2009 Frederik Himpe <fhimpe@mandriva.org> 2.29-1mdv2009.1
+ Revision: 353964
- update to new version 2.29

* Tue Dec 23 2008 Funda Wang <fwang@mandriva.org> 2.28-1mdv2009.1
+ Revision: 317752
- update to new version 2.28

* Wed Nov 12 2008 Funda Wang <fwang@mandriva.org> 2.27-1mdv2009.1
+ Revision: 302492
- update to new version 2.27

* Mon Jul 28 2008 Funda Wang <fwang@mandriva.org> 2.26-1mdv2009.0
+ Revision: 250774
- update to new version 2.26

* Wed May 21 2008 Funda Wang <fwang@mandriva.org> 2.25-1mdv2009.0
+ Revision: 209657
- update to new version 2.25

* Mon Apr 21 2008 Funda Wang <fwang@mandriva.org> 2.24-1mdv2009.0
+ Revision: 196287
- New version 2.24

* Tue Jan 22 2008 Funda Wang <fwang@mandriva.org> 2.23-1mdv2008.1
+ Revision: 156289
- update to new version 2.23

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Dec 16 2007 Funda Wang <fwang@mandriva.org> 2.22-1mdv2008.1
+ Revision: 120483
- New version 2.22

* Thu Nov 01 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2.21-1mdv2008.1
+ Revision: 104491
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - fix description (not a copyright notice, not about build process)

* Tue Oct 09 2007 Funda Wang <fwang@mandriva.org> 2.20-1mdv2008.1
+ Revision: 96028
- New version 2.20

* Tue Aug 07 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2.19-1mdv2008.0
+ Revision: 59848
- better description
- spec file clean
- new version

* Fri Jul 06 2007 Funda Wang <fwang@mandriva.org> 2.18-1mdv2008.0
+ Revision: 48858
- New version

* Thu Jul 05 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 2.17-3mdv2008.0
+ Revision: 48751
- normalize fontpath.d symlink name (based on pkg name)
- fontpath.d conversion (#31756)

* Thu May 17 2007 Funda Wang <fwang@mandriva.org> 2.17-1mdv2008.0
+ Revision: 27536
- New upstream version 2.17

* Sun Apr 29 2007 Funda Wang <fwang@mandriva.org> 2.16-1mdv2008.0
+ Revision: 19133
- New upstream version 2.16


* Thu Mar 15 2007 Olivier Blin <oblin@mandriva.com> 2.15-2mdv2007.1
+ Revision: 144604
- drop huge status.txt file (853k of not useful character/version table)

* Mon Feb 26 2007 Thierry Vignaud <tvignaud@mandriva.com> 2.15-1mdv2007.1
+ Revision: 125924
- new release

* Fri Jan 26 2007 Thierry Vignaud <tvignaud@mandriva.com> 2.14-1mdv2007.1
+ Revision: 113950
- new release

* Mon Nov 20 2006 Thierry Vignaud <tvignaud@mandriva.com> 2.12-1mdv2007.1
+ Revision: 85530
- new release

* Thu Nov 16 2006 Thierry Vignaud <tvignaud@mandriva.com> 2.11-1mdv2007.1
+ Revision: 84975
- new release

* Wed Oct 18 2006 Thierry Vignaud <tvignaud@mandriva.com> 2.10-1mdv2007.1
+ Revision: 66059
- new release

* Wed Sep 06 2006 Thierry Vignaud <tvignaud@mandriva.com> 2.9-1mdv2007.0
+ Revision: 60114
- new release (fix cyrillic issue #25216)

* Sat Aug 05 2006 Helio Chissini de Castro <helio@mandriva.com> 2.8-1mdv2007.0
+ Revision: 52886
- Normalize fonts with new paths
- import fonts-ttf-dejavu-2.8-1mdv2007.0

* Fri Jul 28 2006 Thierry Vignaud <tvignaud@mandriva.com> 2.8-1mdv2007.0
- new release

* Fri Jul 07 2006 Thierry Vignaud <tvignaud@mandriva.com> 2.7-1mdv2007.0
- new release

* Tue May 16 2006 Thierry Vignaud <tvignaud@mandriva.com> 2.6-1mdk
- new release

* Wed Apr 26 2006 Frederic Crozat <fcrozat@mandriva.com> 2.5-1mdk
- Release 2.5 (fix ligature bug with latest pango)

* Tue Mar 07 2006 Thierry Vignaud <tvignaud@mandriva.com> 2.3-1mdk
- new release

* Thu Feb 02 2006 Frederic Crozat <fcrozat@mandriva.com> 2.2-2mdk
- Never ship fonts.cache-2
- fix prereq

* Wed Jan 18 2006 Thierry Vignaud <tvignaud@mandriva.com> 2.2-1mdk
- new release

* Tue Nov 15 2005 Frederic Crozat <fcrozat@mandriva.com> 2.0-2mdk
- fontconfig cache name has changed

* Tue Nov 15 2005 Thierry Vignaud <tvignaud@mandriva.com> 2.0-1mdk
- new release

* Wed Jul 27 2005 Thierry Vignaud <tvignaud@mandriva.com> 1.11-1mdk
- new release

* Thu May 26 2005 Abel Cheung <deaddog@mandriva.org> 1.10-1mdk
- New release 1.10

* Wed May 04 2005 Abel Cheung <deaddog@mandriva.org> 1.9-1mdk
- New release 1.9
- Mark attributes for various files

* Wed Feb 16 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.7-1mdk
- new release

* Tue Nov 02 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.4-1mdk
- new release (merged with Owen & BePa fonts)
- fix package (enable to rebuild on version bumping)

* Tue Aug 10 2004 Robert Vojta <robert.vojta@mandrake.org> 1.1-2mdk
- README file added
- better description (based on the README file)

* Fri Aug 06 2004 Petr Spatka <petr.spatka@kamarad.cz> 1.1-1mdk
- Initial build. Based on fonts-ttf-vera.spec from Mandrake.

