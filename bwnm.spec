Summary:	Simple tool to mount all smb shares
Summary(pl):	Proste narzêdzie do montowania zasobów z smb
Name:		bwnm
Version:	1.1
Release:	1
License:	Freeware
Group:		Applications/Networking
Source0:	http://www-ec.njit.edu/~asm3072/software/%{name}-%{version}.tar.gz
# Source0-md5:	9631a21d80bf8062727e64549301884a
URL:		http://web.njit.edu/~asm3072/programming.html
Requires:	nmap
Requires:	python-modules
Requires:	samba-client
Obsoletes:	wnm
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
bwnm is an altered version of wnm. It uses nmap to find all the
computers in a given IP range with the netbios port open, then using
nmblookup and smbmount it mounts all available shares in the current
directory. wnum allows you to easily unmount those shares.

%description -l pl
bwnm jest now± wersj± wnm. Wykorzystuje nmap-a do znalezienia
wszystkch komputerów pod podanym zakresem IP z otwartymi portami
netbiosu, a nastêpnie wykorzystuj±c nmblookup i smbmount montuje
wszystkie dostêpne zasoby w bierz±cym katalogu. wnum pozwala na ³atwe
odmontowanie tych zasobów.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install bwnm wnum $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
