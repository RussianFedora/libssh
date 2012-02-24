Name:           libssh
Version:        0.5.2
Release:        1%{?dist}
Summary:        A library implementing the SSH2 protocol (0xbadc0de version)

Group:          System Environment/Libraries
License:        LGPLv2+
#original URL:	http://0xbadc0de.be/?part=libssh
URL:            http://www.libssh.org/
Source0:        http://www.libssh.org/files/%{version}/%{name}-%{version}.tar.gz
Source1:        http://www.libssh.org/files/%{version}/%{name}-%{version}.tar.gz.asc
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:  openssl-devel
BuildRequires:  zlib-devel   
BuildRequires:  cmake

%description
The ssh library was designed to be used by programmers needing a
working SSH implementation by the mean of a library. The complete
control of the client is made by the programmer. With libssh, you can
remotely execute programs, transfer files, use a secure and transparent
tunnel for your remote programs. With its Secure FTP implementation,
you can play with remote files easily, without third-party programs
others than libcrypto (from openssl).


%package devel
Summary:         Development files for %{name}
Group:           Development/Libraries
Requires:         %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
mkdir obj
cd obj
%cmake ..
make

%install
rm -rf $RPM_BUILD_ROOT
cd obj
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} + 
chmod 644 $RPM_BUILD_ROOT/usr/include/libssh/*
install -d $RPM_BUILD_ROOT/usr/share
mv $RPM_BUILD_ROOT/%{_libdir}/pkgconfig $RPM_BUILD_ROOT/usr/share

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS BSD ChangeLog COPYING README
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/*.so
%{_usr}/share/pkgconfig/*.pc

%changelog
* Thu Feb 02 2012 Petr Lautrbach <plautrba@redhat.com> 0.5.2-1
- update to 0.5.2 version (#730270)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun  1 2011 Jan F. Chadima <jchadima@redhat.com> - 0.5.0-1
- bounce versionn to 0.5.0 (#709785)
- the support for protocol v1 is disabled

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 19 2011 Jan F. Chadima <jchadima@redhat.com> - 0.4.8-1
- bounce versionn to 0.4.8 (#670456)

* Mon Sep  6 2010 Jan F. Chadima <jchadima@redhat.com> - 0.4.6-1
- bounce versionn to 0.4.6 (#630602)

* Thu Jun  3 2010 Jan F. Chadima <jchadima@redhat.com> - 0.4.4-1
- bounce versionn to 0.4.4 (#598592)

* Wed May 19 2010 Jan F. Chadima <jchadima@redhat.com> - 0.4.3-1
- bounce versionn to 0.4.3 (#593288)

* Tue Mar 16 2010 Jan F. Chadima <jchadima@redhat.com> - 0.4.2-1
- bounce versionn to 0.4.2 (#573972)

* Tue Feb 16 2010 Jan F. Chadima <jchadima@redhat.com> - 0.4.1-1
- bounce versionn to 0.4.1 (#565870)

* Fri Dec 11 2009 Jan F. Chadima <jchadima@redhat.com> - 0.4.0-1
- bounce versionn to 0.4.0 (#541010)

* Thu Nov 26 2009 Jan F. Chadima <jchadima@redhat.com> - 0.3.92-2
- typo in spec file

* Thu Nov 26 2009 Jan F. Chadima <jchadima@redhat.com> - 0.3.92-1
- bounce versionn to 0.3.92 (0.4 beta2) (#541010)

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 0.2-4
- rebuilt with new openssl

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 02 2009 Jan F. Chadima <jchadima@redhat.com> - 0.2-2
- Small changes during review

* Mon Jun 01 2009 Jan F. Chadima <jchadima@redhat.com> - 0.2-1
- Initial build

