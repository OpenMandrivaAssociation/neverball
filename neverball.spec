Name:		neverball
Summary:	NeverBall arcade game
Version: 1.4.0
Release: %mkrel 5
Url:		http://icculus.org/neverball/
Source0:	http://icculus.org/neverball/%{name}-%{version}.tar.bz2
Source1:	%{name}-48.png
Source2:	%{name}-32.png
Source3:	%{name}-16.png
Source4:	neverputt-48.png
Source5:	neverputt-32.png
Source6:	neverputt-16.png
Patch0:		neverball_X11_path.patch
Group:		Games/Arcade
License:	GPL
Epoch:		1
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	SDL_mixer-devel SDL_image-devel SDL_ttf-devel
BuildRequires:	GL-devel
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
%patch0 -p0

%build
%make CFLAGS="$RPM_OPT_FLAGS -ansi `sdl-config --cflags` -L%_prefix/X11R6/%_lib"

%install
rm -rf $RPM_BUILD_ROOT

function install_binary() {
	binary=$1
	install -m755 $binary -D $RPM_BUILD_ROOT%{_gamesbindir}/$binary.bin

	cat > $RPM_BUILD_ROOT%{_gamesbindir}/$binary << EOF
#!/bin/sh
cd %{_gamesdatadir}/%{name}
%{_gamesbindir}/$binary.bin
EOF

	chmod +x $RPM_BUILD_ROOT%{_gamesbindir}/$binary
}

install_binary %{name}
install_binary neverputt

mkdir -p $RPM_BUILD_ROOT%{_gamesdatadir}/%{name}
rm -fr data/map-*/*.map
cp -a data $RPM_BUILD_ROOT%{_gamesdatadir}/%{name}/

install -D -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png
install -D -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -D -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -D -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_liconsdir}/neverputt.png
install -D -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_iconsdir}/neverputt.png
install -D -m 644 %{SOURCE6} $RPM_BUILD_ROOT%{_miconsdir}/neverputt.png

mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat > $RPM_BUILD_ROOT%{_menudir}/%{name} << EOF
?package(%{name}): command="%{_gamesbindir}/%{name}" icon="%{name}.png" section="More Applications/Games/Arcade" title="Neverball" longtitle="Tilt the floor to roll the ball" needs="x11" xdg="true"
?package(%{name}): command="%{_gamesbindir}/neverputt" icon="neverputt.png" section="More Applications/Games/Arcade" title="Neverputt" longtitle="Golf game based on neverball" needs="x11" xdg="true"
EOF
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Neverball
Comment=Tilt the floor to roll the ball
Exec=%{_gamesbindir}/%{name} %U
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Games-Arcade;Game;ArcadeGame;
EOF
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-neverputt.desktop << EOF
[Desktop Entry]
Name=Neverputt
Comment=Golf game based on neverball
Exec=%{_gamesbindir}/neverputt %U
Icon=neverputt
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Games-Arcade;Game;ArcadeGame;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus

%postun
%clean_menus

%files
%defattr(644,root,root,755)
%doc CHANGES README
# do not package TODO to make rpmlint happy (zero size)
%attr(755,root,root) %{_gamesbindir}/%{name}*
%attr(755,root,root) %{_gamesbindir}/neverputt*
%dir %{_gamesdatadir}/%{name}
%{_gamesdatadir}/%{name}/*
%{_datadir}/applications/mandriva*
%{_menudir}/%{name}
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/neverputt.png
%{_iconsdir}/neverputt.png
%{_miconsdir}/neverputt.png

