Name:		neverball
Summary:	Arcade game
Version:    1.5.4
Release:    5
Url:		http://icculus.org/neverball/
Source0:	http://icculus.org/neverball/%{name}-%{version}.tar.bz2
Patch0:		neverball-1.5.2-fix-locale-dir.patch
Patch1:		neverball-1.5.4-fix-linking.patch
Group:		Games/Arcade
License:	GPLv2+
Epoch:		1
BuildRequires:	SDL_mixer-devel SDL_image-devel SDL_ttf-devel pkgconfig(libpng) jpeg-devel
BuildRequires:	pkgconfig(gl)
BuildRequires:	libphysfs-devel
Obsoletes:	neverputt
Provides:	neverputt

%description
Tilt the floor to roll the ball through the obstacle course
before time runs out.
This package inclutes neverputt, a golf game based on neverball.
Hardware accellerated OpenGL support with multitexture
(OpenGL 1.2.1 or greater) is required.

%prep
%setup -q
%apply_patches

%build
%make CFLAGS="%{optflags} -ansi `sdl-config --cflags`" ENABLE_NLS=1 DATADIR=%{_gamesdatadir}/%{name}/data

%install

install -m 755 -D %{name} %{buildroot}%{_gamesbindir}/%{name}
install -m 755 neverputt %{buildroot}%{_gamesbindir}/

mkdir -p %{buildroot}%{_gamesdatadir}/%{name}
rm -fr data/map-*/*.map
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

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc CHANGES README
%doc doc/*
%attr(755,root,root) %{_gamesbindir}/%{name}
%attr(755,root,root) %{_gamesbindir}/neverputt
%dir %{_gamesdatadir}/%{name}
%{_gamesdatadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/neverputt.desktop
%{_datadir}/icons/hicolor/*/apps/never*png
%{_mandir}/man6/neverball.6*
%{_mandir}/man6/neverputt.6*
