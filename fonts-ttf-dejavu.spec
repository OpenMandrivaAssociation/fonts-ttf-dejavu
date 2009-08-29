%define pkgname dejavu-fonts-ttf

Summary: DejaVu ttf Fonts
Name: fonts-ttf-dejavu
Version: 2.30
Release: %mkrel 1
License: Bitstream Vera Fonts Copyright
Group: System/Fonts/True type
URL: http://dejavu.sourceforge.net/
Source0: http://prdownloads.sourceforge.net/dejavu/%{pkgname}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires(post): fontconfig 
Requires(postun): fontconfig 
BuildArch: noarch
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
