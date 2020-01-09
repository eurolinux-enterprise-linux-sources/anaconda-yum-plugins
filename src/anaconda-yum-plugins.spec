Summary: Installation-related yum plugins
Name:    anaconda-yum-plugins
Version: 1.0
Release: 1
License: GPLv2+
Group:   Applications/System
URL:     http://fedoraproject.org/wiki/Anaconda

Source0: %{name}-%{version}.tar.bz2

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
Requires:  python, yum

%description
The anaconda yum-plugins package contains yum plugins that are useful for
anaconda and other system installation-related programs.

%prep
%setup -q

%build
# noop

%install
%{__rm} -rf %{buildroot}
# RPM will take care of the python-compiling stuff
%{__make} install DESTDIR=%{buildroot} NO_PY_COMPILE=1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/*
%{_prefix}/lib/yum-plugins/*

%changelog
* Mon Sep 15 2008 Will Woods <wwoods@redhat.com> - 1.0-1
- Initial packaging (moved out of anaconda package) 
