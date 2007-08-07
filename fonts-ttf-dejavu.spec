%define pkgname dejavu-ttf

Summary: DejaVu ttf Fonts
Name: fonts-ttf-dejavu
Version: 2.19
Release: %mkrel 1
License: Bitstream Vera Fonts Copyright
Group: System/Fonts/True type
URL: http://dejavu.sourceforge.net/
Source0: http://prdownloads.sourceforge.net/dejavu/dejavu-ttf-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires(post): fontconfig 
Requires(postun): fontconfig 
BuildArch: noarch
BuildRequires: freetype-tools

%description
DejaVu fonts are Bitstream Vera fonts (http://www.bitstream.com/) with
additional characters from Latin Extended-A set (Dcaron, dcaron, Ecaron,
ecaron, Lacute, lacute, Lcaron, lcaron, Ncaron, ncaron, Racute, racute,
Rcaron, rcaron, Tcaron, tcaron, Uring, uring). They are optimized for
display on Linux/X (which has some TrueType display problems), but that
should not affect their usability on other systems or in printing.

DejaVu fonts are based on Bitstream Vera fonts version 1.10.

Fonts are (c) Bitstream (see below). DejaVu changes are in public domain.

Fonts are published in source form as SFD files (Spline Font Database from
FontForge - http://fontforge.sf.net/) and in compiled form as TTF files
(TrueType fonts).

%prep
%setup -q -n %{pkgname}-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/fonts/TTF/dejavu

install -m 644 *.ttf $RPM_BUILD_ROOT%{_datadir}/fonts/TTF/dejavu
ttmkfdir $RPM_BUILD_ROOT%{_datadir}/fonts/TTF/dejavu > $RPM_BUILD_ROOT%{_datadir}/fonts/TTF/dejavu/fonts.dir
ln -s fonts.dir $RPM_BUILD_ROOT%{_datadir}/fonts/TTF/dejavu/fonts.scale

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/fonts/TTF/dejavu \
	%{buildroot}%_sysconfdir/X11/fontpath.d/ttf-dejavu:pri=50
%clean
rm -rf $RPM_BUILD_ROOT

%post
fc-cache

%postun
if [ "$1" = "0" ]; then
fc-cache
fi


%files
%defattr(-,root,root,-)
%doc README LICENSE AUTHORS NEWS BUGS *cover.txt
%dir %{_datadir}/fonts/TTF/dejavu
%{_datadir}/fonts/TTF/dejavu/*.ttf
%verify(not mtime) %{_datadir}/fonts/TTF/dejavu/fonts.dir
%{_datadir}/fonts/TTF/dejavu/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-dejavu:pri=50
