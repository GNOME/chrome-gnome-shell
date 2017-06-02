Name:           chrome-gnome-shell
Version:        9
Release:        1%{?dist}
Summary:        GNOME Shell integration for Chrome

License:        GPLv3+
URL:            https://wiki.gnome.org/Projects/GnomeShellIntegrationForChrome
Source0:        https://git.gnome.org/browse/%{name}/snapshot/%{name}-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  jq
BuildRequires:  python2-devel
Requires:       gnome-shell
Requires:       python-gobject-base
Requires:       python-requests

%description
Browser extension for Google Chrome/Chromium, Firefox, Vivaldi, Opera
(and other Browser Extension, Chrome Extension or WebExtensions capable
browsers) and native host messaging connector that provides integration
with GNOME Shell and the corresponding extensions repository
https://extensions.gnome.org.

%prep
%autosetup

%build
mkdir build
pushd build
  %cmake .. \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
    -DBUILD_EXTENSION=OFF
  %make_build
popd

%install
pushd build
  %make_install
popd

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.ChromeGnomeShell.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/chrome-gnome-shell
%{_datadir}/applications/org.gnome.ChromeGnomeShell.desktop
%{_datadir}/dbus-1/services/org.gnome.ChromeGnomeShell.service
%{_datadir}/icons/gnome/*/*/org.gnome.ChromeGnomeShell.png
%dir %{_sysconfdir}/chromium
%dir %{_sysconfdir}/chromium/native-messaging-hosts
%dir %{_sysconfdir}/chromium/policies
%dir %{_sysconfdir}/chromium/policies/managed
%config(noreplace) %{_sysconfdir}/chromium/native-messaging-hosts/org.gnome.chrome_gnome_shell.json
%config(noreplace) %{_sysconfdir}/chromium/policies/managed/chrome-gnome-shell.json
%dir %{_sysconfdir}/opt/chrome
%dir %{_sysconfdir}/opt/chrome/native-messaging-hosts
%dir %{_sysconfdir}/opt/chrome/policies
%dir %{_sysconfdir}/opt/chrome/policies/managed
%config(noreplace) %{_sysconfdir}/opt/chrome/native-messaging-hosts/org.gnome.chrome_gnome_shell.json
%config(noreplace) %{_sysconfdir}/opt/chrome/policies/managed/chrome-gnome-shell.json
%{_libdir}/mozilla/native-messaging-hosts/org.gnome.chrome_gnome_shell.json
%{python2_sitelib}/chrome_gnome_shell-*.egg-info

%changelog
* Thu Apr 20 2017 Maxim Orlov <murmansksity@gmail.com> - 9-1
- Update to Ver.9

* Sun Apr 02 2017 Maxim Orlov <murmansksity@gmail.com> - 8.2.1-1
- Update to Ver.8.2.1

* Fri Mar 03 2017 Maxim Orlov <murmansksity@gmail.com> - 8.2-1
- Update to Ver.8.2

* Wed Feb 22 2017 Maxim Orlov <murmansksity@gmail.com> - 8.1-1
- Update to Ver.8.1

* Sun Jan 22 2017 Maxim Orlov <murmansksity@gmail.com> - 8-1
- Update to Ver.8

* Mon Dec 26 2016 Maxim Orlov <murmansksity@gmail.com> - 7.2.1-1
- Update to Ver.7.2.1

* Sat Nov 19 2016 Maxim Orlov <murmansksity@gmail.com> - 7.2-1
- Update to Ver.7.2

* Mon Sep 26 2016 Maxim Orlov <murmansksity@gmail.com> - 7.1-1
- Update to Ver.7.1

* Thu Sep 08 2016 Maxim Orlov <murmansksity@gmail.com> - 7-1
- Update to Ver.7

* Sat Aug 06 2016 Maxim Orlov <murmansksity@gmail.com> - 6.2-1
- Update to Ver.6.2

* Sun Jul 31 2016 Maxim Orlov <murmansksity@gmail.com> - 6.1-2
- Add missing Requires: python-gobject-base

* Tue Jun 07 2016 Maxim Orlov <murmansksity@gmail.com> - 6.1-1
- Update to Ver.6.1

* Sat May 14 2016 Maxim Orlov <murmansksity@gmail.com> - 6-1
- Update to Ver.6
- Fix "orphaned directory"

* Mon Apr 11 2016 Maxim Orlov <murmansksity@gmail.com> - 5.2-1
- Initial package.
