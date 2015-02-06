Name:           qshare
Version:        2.1.5
Release:        2
License:        GPLv3
Url:		http://www.zuzuf.net/qshare
Source0:	http://www.zuzuf.net/qshare/files/%{name}-%{version}-src.tar.bz2
Group:		File tools
Summary:        Qt file share
BuildRequires:  gcc-c++ pkgconfig(libxml-2.0)
BuildRequires:  qt4-devel avahi-compat-libdns_sd-devel
BuildRequires:  cmake
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
%setup -q

%build
#% qmake_qt4
%cmake
%make

#% find_lang %{name}

%install
%makeinstall_std -C build/ INSTALL_ROOT=%{buildroot}%{_prefix}

%files
%doc AUTHORS README COPYING
%{_datadir}/%{name}
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
#% {_datadir}/icons/*
