Summary: 	Greenbone Security Desktop
Name:		gsd
Version:	1.1.1
Release:	%mkrel 1
Source:		http://wald.intevation.org/frs/download.php/561/%name-%version.tar.gz
Patch0:		openvas-administrator-1.1.1-build.patch
Group:		System/Configuration/Networking
Url:		http://www.openvas.org
License:	GPLv2+
BuildRoot:	%{_tmppath}/%name-%{version}-root
BuildRequires:	cmake
BuildRequires:	openvas-devel >= 4.0

%description

%prep
%setup -q -n %name-%version

sed -i -e 's#-Werror##' CMakeLists.txt

%build
%cmake -DSYSCONFDIR=%{_sysconfdir}
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/openvas/gsd_log.conf
%{_bindir}/gsd
%{_mandir}/man8/gsd.8*
%{_datadir}/openvas/translations/gsd_*.qm
