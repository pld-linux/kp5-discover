%define		kdeplasmaver	5.23.0
%define		qtver		5.9.0
%define		kpname		discover
Summary:	discover
Name:		kp5-%{kpname}
Version:	5.23.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	e2b8aff203d8d7c746a226c6a2e10eb4
URL:		http://www.kde.org/
BuildRequires:	Qt5Concurrent-devel >= %{qtver}
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Network-devel >= %{qtver}
BuildRequires:	Qt5Qml-devel >= %{qtver}
BuildRequires:	Qt5Quick-devel >= %{qtver}
BuildRequires:	Qt5Svg-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	Qt5Xml-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	kf5-karchive-devel
BuildRequires:	kf5-kconfig-devel
BuildRequires:	kf5-kconfigwidgets-devel
BuildRequires:	kf5-kcoreaddons-devel
BuildRequires:	kf5-kdbusaddons-devel
BuildRequires:	kf5-kdeclarative-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kiconthemes-devel
BuildRequires:	kf5-kidletime-devel
BuildRequires:	kf5-kio-devel
BuildRequires:	kf5-kitemmodels-devel
BuildRequires:	kf5-kitemviews-devel
BuildRequires:	kf5-knewstuff-devel
BuildRequires:	kf5-knotifications-devel
BuildRequires:	kf5-ktextwidgets-devel
BuildRequires:	kf5-kwallet-devel
BuildRequires:	kf5-kwidgetsaddons-devel
BuildRequires:	kf5-solid-devel
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
discover

%prep
%setup -q -n %{kpname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang discover --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f discover.lang
%defattr(644,root,root,755)
%dir %{_libdir}/qt5/plugins/discover
%attr(755,root,root) %{_libdir}/qt5/plugins/discover/kns-backend.so
%{_desktopdir}/org.kde.discover.desktop
%attr(755,root,root) %{_bindir}/plasma-discover
%{_libdir}/plasma-discover
%{_desktopdir}/org.kde.discover.urlhandler.desktop
%{_iconsdir}/hicolor/128x128/apps/plasmadiscover.png
%{_iconsdir}/hicolor/16x16/apps/plasmadiscover.png
%{_iconsdir}/hicolor/22x22/apps/plasmadiscover.png
%{_iconsdir}/hicolor/32x32/apps/plasmadiscover.png
%{_iconsdir}/hicolor/48x48/apps/plasmadiscover.png
%{_iconsdir}/hicolor/scalable/apps/plasmadiscover.svg*
%dir %{_datadir}/kxmlgui5/plasmadiscover
%{_datadir}/kxmlgui5/plasmadiscover/plasmadiscoverui.rc
%{_datadir}/metainfo/org.kde.discover.appdata.xml
/etc/xdg/autostart/org.kde.discover.notifier.desktop
%attr(755,root,root) %{_libexecdir}/DiscoverNotifier
%{_desktopdir}/org.kde.discover.notifier.desktop
%{_datadir}/knotifications5/discoverabstractnotifier.notifyrc
%{_datadir}/qlogging-categories5/discover.categories
%attr(755,root,root) %{_bindir}/plasma-discover-update
%attr(755,root,root) %{_libdir}/qt5/plugins/kcms/kcm_updates.so
%{_desktopdir}/org.kde.discover.snap.desktop
%dir %{_datadir}/kpackage/kcms/kcm_updates
%dir %{_datadir}/kpackage/kcms/kcm_updates/contents
%dir %{_datadir}/kpackage/kcms/kcm_updates/contents/ui
%{_datadir}/kpackage/kcms/kcm_updates/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcm_updates/metadata.desktop
%{_datadir}/kpackage/kcms/kcm_updates/metadata.json
%{_datadir}/kservices5/kcm_updates.desktop
