Summary:	Arcade game
Name:		neverball
Version:	1.6.0
Release:	2
Epoch:		1
License:	GPLv2+
Group:		Games/Arcade
Url:		http://icculus.org/neverball/
Source0:	http://icculus.org/neverball/%{name}-%{version}.tar.gz
BuildRequires:	jpeg-devel
BuildRequires:	libphysfs-devel
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	pkgconfig(SDL2_ttf)
BuildRequires:	pkgconfig(vorbisfile)

%description
Tilt the floor to roll the ball through the obstacle course before time
runs out.

This package inclutes neverputt, a golf game based on neverball.

Hardware accellerated OpenGL support with multitexture (OpenGL 1.2.1
or greater) is required.

%files -f %{name}.lang
%doc LICENSE.md README.md
%doc doc/*
%{_gamesbindir}/%{name}
%{_gamesbindir}/neverputt
%dir %{_gamesdatadir}/%{name}
%{_gamesdatadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/neverputt.desktop
%{_datadir}/icons/hicolor/*/apps/never*png
%{_mandir}/man6/neverball.6*
%{_mandir}/man6/neverputt.6*

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%make \
	CFLAGS="%{optflags}" \
	CXXFLAGS="%{optflags}" \
	ENABLE_NLS=1 \
	DATADIR=%{_gamesdatadir}/%{name}/data \
	LOCALEDIR=%{_datadir}/locale

%install
install -m 755 -D %{name} %{buildroot}%{_gamesbindir}/%{name}
install -m 755 neverputt %{buildroot}%{_gamesbindir}/

mkdir -p %{buildroot}%{_gamesdatadir}/%{name}
rm -fr data/map-*/*.map
find data -perm 0600 | xargs chmod 0644
cp -a data %{buildroot}%{_gamesdatadir}/%{name}/

mkdir -p %{buildroot}%{_datadir}/applications
install -m 644 dist/*.desktop %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_mandir}/man6
install -m 644 dist/*.6 %{buildroot}%{_mandir}/man6

for res in 16 24 32 48 64 128 256; do
	mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${res}x${res}/apps
	install -m 644 dist/neverball_${res}.png %{buildroot}%{_datadir}/icons/hicolor/${res}x${res}/apps/neverball.png
	install -m 644 dist/neverputt_${res}.png %{buildroot}%{_datadir}/icons/hicolor/${res}x${res}/apps/neverputt.png
done

cp -r locale %{buildroot}%{_datadir}/

%find_lang %{name}

