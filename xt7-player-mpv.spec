# First release based on mpv 
# New versioning, and new deps.

%define mpv_version 0.8.3
%define gba_version 362
%define version %{mpv_version}%{gba_version}
%define oname xt7-player-mpv

Summary:	Xt7-player mpv GUI
Name:		%{oname}
Version:	%{version}
Release:	1
URL:		http://xt7-player.sourceforge.net/xt7forum/
Source:		https://github.com/kokoko3k/xt7-player-mpv/archive/%{version}.tar.gz
Source100:	%{oname}.rpmlintrc
License:	GPLv2
Group:		Video
BuildArch:	noarch

BuildRequires:	gambas3-devel >= 3.6.2
BuildRequires:	gambas3-runtime >= 3.6.2
BuildRequires:	gambas3-gb-qt4 >= 3.6.2
BuildRequires:	gambas3-gb-form >= 3.6.2
BuildRequires:	gambas3-gb-desktop >= 3.6.2
BuildRequires:	gambas3-gb-form-mdi >= 3.6.2
BuildRequires:	gambas3-gb-net >= 3.6.2
BuildRequires:	gambas3-gb-net-curl >= 3.6.2
BuildRequires:	gambas3-gb-settings >= 3.6.2
BuildRequires:	gambas3-gb-xml >= 3.6.2
BuildRequires:	gambas3-gb-web >= 3.6.2
BuildRequires:	gambas3-gb-image >= 3.6.2
BuildRequires:	gambas3-gb-image-imlib >= 3.6.2
BuildRequires:	gambas3-gb-image-io >= 3.6.2
BuildRequires:	gambas3-gb-db >= 3.6.2
BuildRequires:	gambas3-gb-dbus >= 3.6.2
BuildRequires:	gambas3-gb-db-form >= 3.6.2
BuildRequires:	gambas3-gb-qt4-ext >= 3.6.2
BuildRequires:	pkgconfig(taglib)
BuildRequires:	gambas3-gb-gui >= 3.6.2
BuildRequires:	gambas3-gb-compress >= 3.6.2
BuildRequires:	gambas3-gb-form-dialog >= 3.6.2
BuildRequires:	gambas3-gb-signal >= 3.6.2
BuildRequires:	gambas3-gb-libxml >= 3.6.2
BuildRequires:	gambas3-gb-form-stock  >= 3.6.2

# 4 desktop file install/check
BuildRequires:	desktop-file-utils

# 4 icons convert
BuildRequires:	imagemagick

# 4 dvb-epg
Requires:	dvbsnoop
Requires:	dvb-apps

# 4 downloading from youtube
Requires:	config(youtube-dl) >= 2015.03.09
Requires:	xterm
Requires:	wget

# 4 audio extract/convert
Requires:	ffmpeg

# 4 subtiles , manage, download a.s.o.
Requires:	python >= 2.7

# 4 global hotkeys support
Requires:	xbindkeys

# 4 desktop integration
Requires:	xdg-utils

# 4 tagging
Requires:	%{_lib}taglib1
Requires:	%{_lib}taglib_c0

# default player
Requires:	mpv >= 0.8.2

# 4 GUI
Requires:	gambas3-runtime >= 3.6.2
Requires:	gambas3-gb-image >= 3.6.2
Requires:	gambas3-gb-dbus >= 3.6.2
Requires:	gambas3-gb-qt4 >= 3.6.2
Requires:	gambas3-gb-gtk >= 3.6.2
Requires:	gambas3-gb-gui >= 3.6.2
Requires:	gambas3-gb-form >= 3.6.2
Requires:	gambas3-gb-xml >= 3.6.2
Requires:	gambas3-gb-qt4-ext >= 3.6.2
Requires:	gambas3-gb-form-stock  >= 3.6.2
Requires:	gambas3-gb-net >= 3.6.2
Requires:	gambas3-gb-form-dialog >= 3.6.2
Requires:	gambas3-gb-settings >= 3.6.2
Requires:	gambas3-gb-form-mdi >= 3.6.2
Requires:	gambas3-gb-compress >= 3.6.2
Requires:	gambas3-gb-desktop >= 3.6.2
Requires:	gambas3-gb-web >= 3.6.2
Requires:	gambas3-gb-net-curl >= 3.6.2
Requires:	gambas3-gb-signal >= 3.6.2

# 4 icecast
Requires:	gambas3-gb-libxml >= 3.6.2

Provides:	Xt7-player3
Provides:	xt7-player3
Obsoletes: xt7-player3 
Obsoletes: Xt7-player3

AutoReqProv:	no

%description
Xt7-Player, an (almost) complete mplayer GUI
This program is written in Gambas3, so you will need Gambas3 to be installed.

%prep
%setup -qn %{oname}-%{version}

%build
gbc3 -e -a -g -t -p -m
gba3

%install
mkdir -p %{buildroot}%{_bindir}
install -m755 %{oname}-%{version}.gambas %{buildroot}%{_bindir}/%{oname}.gambas


#icons
install -d -m755 %{buildroot}{%{_miconsdir},%{_iconsdir},%{_liconsdir}}
convert %{oname}.png -resize 32x32 %{buildroot}%{_iconsdir}/%{oname}.png
convert %{oname}.png -resize 16x16 %{buildroot}%{_miconsdir}/%{oname}.png
install -p %{oname}.png %{buildroot}%{_liconsdir}/%{oname}.png



#menu entry
desktop-file-install  %{oname}.desktop\
	--dir %{buildroot}%{_datadir}/applications


%files
%doc COPYING README CHANGELOG_GIT
%{_bindir}/*
%{_iconsdir}/%{oname}.png
%{_miconsdir}/%{oname}.png
%{_liconsdir}/%{oname}.png
%{_datadir}/applications/%{oname}.desktop






