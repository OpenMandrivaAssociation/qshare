Name:           qshare
Version:        2.1.2
Release:        1
License:        GPLv3
Url:		http://www.zuzuf.net/qshare
Source0:	http://www.zuzuf.net/qshare/files/%{name}-%{version}-src.tar.gz
Group:		File tools
Summary:        Qt file share
BuildRequires:  gcc-c++ libxml2-devel
BuildRequires:  qt4-devel avahi-compat-libdns_sd-devel
Requires:       avahi

%description
qShare is a FTP server with a built-in service discovery feature that makes
qShare clients aware of other clients running on the same network. It also
supports Zeroconf on Linux. You can easily add/remove folders from the shared
folders list, set access rights, toggle password protection, etc...
 
The most useful feature is probably the file search feature. The built-in FTP
server implements a FIND command used by qShare to look for files on all known
computers of the network with very little network/CPU overload.

%prep
%setup -q -n %{name}

%build
%qmake_qt4
%make

%install
%makeinstall_std INSTALL_ROOT=%{buildroot}%{_prefix}

%files 
%doc AUTHORS README COPYING
%{_bindir}/%{name}


%changelog
* Fri Jan 20 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.1.2-1
+ Revision: 762906
- BR:avahi-compat-libdns_sd-devel
- imported package qshare

