#
%define		_state		snapshots
%define		_ver		3.2.90
%define		_snap		040110

Summary:	Web development tools for KDE
Summary(es):	Uno editor WEB para KDE
Summary(pl):	Narzêdzia do tworzenia WWW dla KDE
Summary(pt_BR):	Um editor web para o KDE
Name:		kdewebdev
Version:	%{_ver}
Release:	0.1
Epoch:		1
License:	GPL
Group:		X11/Development/Tools
#Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{name}-%{_snap}.tar.bz2
Source0:	http://ep09.pld-linux.org/~adgor/kde/%{name}.tar.bz2
##%% Source0-md5:	77f2e92edd4caf70703b7274a461ef42
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1.6.1
BuildRequires:	kdelibs-devel >= 9:%{version}
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	unsermake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Quanta Plus is a web development tool for the K Desktop Environment.
Quanta is designed for quick web development and is rapidly becoming a
mature editor with a number of great features.

%description -l es
Quanta Plus és una herramienta de desarrollo web para KDE. Es
projetado para rapido desarrollo web e es casi pronto com excelent
quantidad de caracteristicas.

%description -l pl
Quanta Plus to narzêdzie do tworzenia WWW dla ¶rodowiska KDE. S³u¿y do
szybkiego tworzenia stron i staje siê dojrza³ym edytorem z wieloma
przydatnymi mo¿liwo¶ciami.

%description -l pt_BR
O Quanta Plus é uma ferramenta para desenvolvimento web para o KDE. É
projetado para desenvolvimento web rápido e está rapidamente se
tornando um editor maduro com um bom número de excelentes
características.

%package devel
Summary:	Header files for Quanta libraries
Summary(pl):	Pliki nag³ówkowe bibliotek Quanty
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files for Quanta libraries.

%description devel -l pl
Pliki nag³ówkowe bibliotek Quanty.

%package kfilereplace
Summary:	TODO
Summary(pl):	TODO
Group:		X11/Development/Tools
#Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	quanta < 1:3.2.90

%description kfilereplace
TODO.

%description kfilereplace -l pl
TODO.

%package kommander
Summary:	TODO
Summary(pl):	TODO
Group:		X11/Development/Tools
#Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	quanta < 1:3.2.90

%description kommander
TODO.

%description kommander -l pl
TODO.

%package kxsldbg
Summary:	TODO
Summary(pl):	TODO
Group:		X11/Development/Tools
#Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	quanta < 1:3.2.90

%description kxsldbg
TODO.

%description kxsldbg -l pl
TODO.

%package quanta
Summary:	TODO
Summary(pl):	TODO
Group:		X11/Development/Tools
#Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	quanta

%description quanta
TODO.

%description quanta -l pl
TODO.

%prep
%setup -q -n %{name}

%build
cp -f /usr/share/automake/config.sub admin

export UNSERMAKE=/usr/share/unsermake/unsermake 

%{__make} -f admin/Makefile.common cvs

%configure \
	--disable-rpath \
	--enable-final \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

# Debian manpages
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install debian/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

install -d $RPM_BUILD_ROOT%{_desktopdir}/kde

mv $RPM_BUILD_ROOT%{_datadir}/applnk/{Development/*,Utilities/*} \
	$RPM_BUILD_ROOT%{_desktopdir}/kde
echo "Categories=Qt;KDE;Development;" >> $RPM_BUILD_ROOT%{_desktopdir}/kde/kxsldbg.desktop
echo "Categories=Qt;KDE;Utility;" >> $RPM_BUILD_ROOT%{_desktopdir}/kde/kfilereplacepart.desktop

%find_lang kxsldbg --with-kde
%find_lang quanta --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkommanderwidgets.so
%attr(755,root,root) %{_libdir}/libqtnotfier.so
%attr(755,root,root) %{_libdir}/libxsldbg.so
%{_includedir}/kxsldbg_partif.h
%{_includedir}/kxsldbgif.h

%files kfilereplace
%defattr(644,root,root,755)

%files kommander
%defattr(644,root,root,755)

%files kxsldbg -f kxsldbg.lang
%defattr(644,root,root,755)

%files quanta -f quanta.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/quanta

%{_libdir}/libkommanderwidgets.la
%attr(755,root,root) %{_libdir}/libkommanderwidgets.so.*.*.*
%{_libdir}/libqtnotfier.la
%attr(755,root,root) %{_libdir}/libqtnotfier.so.*.*.*
%{_libdir}/libxsldbg.la
%attr(755,root,root) %{_libdir}/libxsldbg.so.*.*.*

%{_libdir}/kde3/libkfilereplacepart.la
%attr(755,root,root) %{_libdir}/kde3/libkfilereplacepart.so*
%{_libdir}/kde3/libkxsldbgpart.la
%attr(755,root,root) %{_libdir}/kde3/libkxsldbgpart.so*

#%dir %{_libdir}/quanta
#%dir %{_libdir}/quanta/plugins
#%attr(755,root,root) %{_libdir}/quanta/plugins/weblint
%{_datadir}/apps/kafkapart
%dir %{_datadir}/apps/kfilereplacepart
%{_datadir}/apps/kfilereplacepart/*
%dir %{_datadir}/apps/kxsldbg
%{_datadir}/apps/kxsldbg/kxsldbg_shell.rc
%dir %{_datadir}/apps/kxsldbgpart
%{_datadir}/apps/kxsldbgpart/kxsldbg_part.rc
%dir %{_datadir}/apps/quanta

%{_datadir}/apps/quanta/csseditor
%{_datadir}/apps/quanta/dtep
#%{_datadir}/apps/quanta/plugins
%{_datadir}/apps/quanta/scripts
%{_datadir}/apps/quanta/templates
%{_datadir}/apps/quanta/toolbar
%{_datadir}/apps/quanta/toolbars
%{_datadir}/apps/quanta/actions.rc
%{_datadir}/apps/quanta/chars
%{_datadir}/apps/quanta/plugins.rc
%{_datadir}/apps/quanta/quantaui.rc
%{_datadir}/apps/quanta/tips
# !!!
%{_datadir}/apps/templates
#
%{_datadir}/mimelnk/application/x-kommander.desktop
%{_datadir}/services/kfilereplacepart.desktop
%{_datadir}/services/kxsldbg_part.desktop
%{_desktopdir}/kde/*
%{_iconsdir}/[!l]*/*/*/*
%{_mandir}/man1/*.1*
