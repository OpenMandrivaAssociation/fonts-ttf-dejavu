%define pkgname dejavu-fonts-ttf

Summary:	DejaVu ttf Fonts
Name:		fonts-ttf-dejavu
Version:	2.37
Release:	2
License:	Bitstream Vera Fonts Copyright
Group:		System/Fonts/True type
Url:		http://dejavu.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/dejavu/%{pkgname}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	fontconfig
BuildRequires:	freetype-tools

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
%setup -qn %{pkgname}-%{version}

%build
# (tpg) nothing to do here unless we decide to build fonts from sources

%install
mkdir -p %{buildroot}%{_datadir}/fonts/TTF/dejavu

install -m 644 ttf/*.ttf %{buildroot}%{_datadir}/fonts/TTF/dejavu
ttmkfdir %{buildroot}%{_datadir}/fonts/TTF/dejavu > %{buildroot}%{_datadir}/fonts/TTF/dejavu/fonts.dir
ln -s fonts.dir %{buildroot}%{_datadir}/fonts/TTF/dejavu/fonts.scale

mkdir -p %{buildroot}%{_sysconfdir}/X11/fontpath.d/
ln -s ../../..%{_datadir}/fonts/TTF/dejavu \
	%{buildroot}%{_sysconfdir}/X11/fontpath.d/ttf-dejavu:pri=50

%files
%doc LICENSE AUTHORS NEWS BUGS *cover.txt
%dir %{_datadir}/fonts/TTF/dejavu
%{_datadir}/fonts/TTF/dejavu/*.ttf
%verify(not mtime) %{_datadir}/fonts/TTF/dejavu/fonts.dir
%{_datadir}/fonts/TTF/dejavu/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-dejavu:pri=50

