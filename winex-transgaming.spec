Summary:	Program that lets you launch Win applications
Summary(es):	Ejecuta programas Windows en Linux
Summary(pl):	Program pozwalaj±cy uruchamiaæ aplikacje Windows
Summary(pt_BR):	Executa programas Windows no Linux
Name:		winex-transgaming
Version:	3.3.2
Release:	1
License:	custom, non-distributable
Group:		Applications/Emulators
Source0:	winex3_%{version}-1.i386.tgz
# NoSource0-md5: 925950091ac3ce9c9eb648a7d707a69d
URL:		http://www.transgaming.com/
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep		libGL.so.1 libGLU.so.1
%define		no_install_post_strip	1

%description
Wine is a program which allows running Microsoft Windows programs
(including DOS, Windows 3.x and Win32 executables) on Unix. It
consists of a program loader which loads and executes a Microsoft
Windows binary, and a library that implements Windows API calls using
their Unix or X11 equivalents. The library may also be used for
porting Win32 code into native Unix executables.

%description -l es
Ejecuta programas Windows en Linux.

%description -l pl
Wine jest programem dziêki któremu mo¿na uruchamiaæ programy napisane
dla Microsoft Windows pod systemami unixowymi. Sk³ada siê on z
loadera, który pozwala wczytywaæ i uruchamiaæ programy w formacie
Microsoft Windows oraz z biblioteki, która implementuje API Windows
przy u¿yciu odpowiedników Unixowych oraz z X11. Biblioteka mo¿e byæ
tak¿e wykorzystana do przenoszenia aplikacji Win32 na Uniksa.

%description -l pt_BR
O Wine é um programa que permite rodar programas MS-Windows no X11.
Ele consiste de um carregador de programa, que carrega e executa um
binário MS-Windows, e de uma biblioteca de emulação que traduz as
chamadas da API para as equivalentes Unix/X11.

%prep
%setup -q -c

%build
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}
cp -r * $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/winex3
%dir %{_libdir}/transgaming_winex3
%{_libdir}/transgaming_winex3/update.reg
%attr(755,root,root) %{_libdir}/transgaming_winex3/.transgaming
%dir %{_libdir}/transgaming_winex3/winex
%dir %{_libdir}/transgaming_winex3/winex/lib
%attr(755,root,root) %{_libdir}/transgaming_winex3/winex/lib/*
%dir %{_libdir}/transgaming_winex3/winex/bin
%attr(755,root,root) %{_libdir}/transgaming_winex3/winex/bin/*
%dir %{_libdir}/transgaming_winex3/winex/pthread_lib
%attr(755,root,root) %{_libdir}/transgaming_winex3/winex/pthread_lib/*
%doc usr/share/doc/winex3/*
