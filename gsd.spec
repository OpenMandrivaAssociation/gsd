Summary: 	Greenbone Security Desktop
Name:		gsd
Version:	1.2.2
Release:	1
Source0:		http://wald.intevation.org/frs/download.php/561/%name-%version.tar.gz
patch1:		gsd-1.2.2.ompentity.patch
Group:		System/Configuration/Networking
Url:		http://www.openvas.org
License:	GPLv2+
BuildRequires:	cmake
BuildRequires:	openvas-devel >= 4.0
BuildRequires:	doxygen
BuildRequires:	qt4-devel
Requires:	openvas-manager

%description
The GSD is a desktop client that connects to the OpenVAS Manager using
the OMP protocol.

It uses the Qt framework for the GUI and is implemented in C++.  Main
dependencies are qt4, gnutls, glib and openvas-libraries.

%prep
%setup -q -n %name-%version
%patch1 -p1 -b .ompentity

sed -i -e 's#-Werror##' CMakeLists.txt

%build
export LDFLAGS="-lopenvas_misc -lglib-2.0 -lgnutls"
%cmake -DSYSCONFDIR=%{_sysconfdir}
%make

%install
%makeinstall_std -C build

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/openvas/gsd_log.conf
%{_bindir}/gsd
%{_mandir}/man8/gsd.8*
%{_datadir}/openvas/*.html
%{_datadir}/openvas/translations/gsd_*.qm


%changelog
* Mon May 23 2011 Funda Wang <fwang@mandriva.org> 1.2.0-1mdv2011.0
+ Revision: 677475
- new version 1.2.0

* Sat Apr 02 2011 Funda Wang <fwang@mandriva.org> 1.1.1-1
+ Revision: 649838
- add desc
- add BR
- import gsd

