%define mpv_version 0.11
%define gba_version 381
%define version %{mpv_version}.%{gba_version}
%define oname xt7-player-mpv
%define  _appdatadir %{_datadir}/appdata


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

BuildRequires:	gambas3-devel >= 3.8.1
BuildRequires:	gambas3-runtime >= 3.8.1
BuildRequires:	gambas3-gb-qt4 >= 3.8.1
BuildRequires:	gambas3-gb-form >= 3.8.1
BuildRequires:	gambas3-gb-desktop >= 3.8.1
BuildRequires:	gambas3-gb-form-mdi >= 3.8.1
BuildRequires:	gambas3-gb-net >= 3.8.1
BuildRequires:	gambas3-gb-net-curl >= 3.8.1
BuildRequires:	gambas3-gb-settings >= 3.8.1
BuildRequires:	gambas3-gb-xml >= 3.8.1
BuildRequires:	gambas3-gb-web >= 3.8.1
BuildRequires:	gambas3-gb-image >= 3.8.1
BuildRequires:	gambas3-gb-image-imlib >= 3.8.1
BuildRequires:	gambas3-gb-image-io >= 3.8.1
BuildRequires:	gambas3-gb-db >= 3.8.1
BuildRequires:	gambas3-gb-dbus >= 3.8.1
BuildRequires:	gambas3-gb-db-form >= 3.8.1
BuildRequires:	gambas3-gb-qt4-ext >= 3.8.1
BuildRequires:	pkgconfig(taglib)
BuildRequires:	gambas3-gb-gui >= 3.8.1
BuildRequires:	gambas3-gb-compress >= 3.8.1
BuildRequires:	gambas3-gb-form-dialog >= 3.8.1
BuildRequires:	gambas3-gb-signal >= 3.8.1
BuildRequires:	gambas3-gb-libxml >= 3.8.1
BuildRequires:	gambas3-gb-form-stock  >= 3.8.1
BuildRequires:	gambas3-gb-util-web >= 3.8.1
BuildRequires:	gambas3-gb-args >= 3.8.1

# 4 desktop file install/check
BuildRequires:	desktop-file-utils

# 4 appdata file
BuildRequires:	appstream-util

# 4 icons convert
BuildRequires:	imagemagick



# 4 dvb-epg
Requires:	dvbsnoop
Requires:	dvb-apps

# 4 downloading from youtube
Requires:	config(youtube-dl) >= 2015.07.28
Requires:	xterm
Requires:	wget
Requires:	gambas3-gb-util-web >= 3.8.1

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
Requires:	mpv >= 0.11.0

# 4 GUI
Requires:	gambas3-runtime >= 3.8.1
Requires:	gambas3-gb-image >= 3.8.1
Requires:	gambas3-gb-dbus >= 3.8.1
Requires:	gambas3-gb-qt4 >= 3.8.1
Requires:	gambas3-gb-gtk >= 3.8.1
Requires:	gambas3-gb-gui >= 3.8.1
Requires:	gambas3-gb-form >= 3.8.1
Requires:	gambas3-gb-xml >= 3.8.1
Requires:	gambas3-gb-qt4-ext >= 3.8.1
Requires:	gambas3-gb-form-stock  >= 3.8.1
Requires:	gambas3-gb-net >= 3.8.1
Requires:	gambas3-gb-form-dialog >= 3.8.1
Requires:	gambas3-gb-settings >= 3.8.1
Requires:	gambas3-gb-form-mdi >= 3.8.1
Requires:	gambas3-gb-compress >= 3.8.1
Requires:	gambas3-gb-desktop >= 3.8.1
Requires:	gambas3-gb-web >= 3.8.1
Requires:	gambas3-gb-net-curl >= 3.8.1
Requires:	gambas3-gb-signal >= 3.8.1
Requires:	gambas3-gb-args >= 3.8.1

# 4 icecast / shoutcast
Requires:	gambas3-gb-libxml >= 3.8.1

Provides:	Xt7-player3 = %{EVRD}
Provides:	xt7-player3 = %{EVRD}

Obsoletes: xt7-player3 < %{EVRD}  
Obsoletes: Xt7-player3 < %{EVRD}

AutoReqProv:	no

%description
Xt7-Player, an complete mpv GUI
This program is written in Gambas3, so you will need Gambas3 to be installed.

%prep
%setup -qn %{oname}-%{version}

%build
gbc3 -e -a -g -t -p -m
gba3

%install
# executable
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
	
#appdata
mkdir -p %{buildroot}%{_appdatadir}
cp -R xt7-player-mpv.appdata.xml %{buildroot}%{_appdatadir}/xt7-player-mpv.appdata.xml
appstream-util validate-relax --nonet %{buildroot}%{_appdatadir}/*.xml	

%files
%doc COPYING README CHANGELOG_GIT
%{_bindir}/*
%{_iconsdir}/%{oname}.png
%{_miconsdir}/%{oname}.png
%{_liconsdir}/%{oname}.png
%{_datadir}/applications/%{oname}.desktop
%{_appdatadir}/*.appdata.xml