# TODO
# - missing icon: kxsldbg, kommander
# - missing icon for 'Webdesign' kde menu (not this package related, but still)

%define		_state		stable
%define		_kdever		3.4.2
%define		_ver		3.4.2

%define		_minlibsevr	9:3.4.2
%define		_minbaseevr	9:3.4.2

Summary:	Web development tools for KDE
Summary(es):	Uno editor WEB para KDE
Summary(pl):	Narzêdzia do tworzenia WWW dla KDE
Summary(pt_BR):	Um editor web para o KDE
Name:		kdewebdev
Version:	%{_ver}
Release:	1
Epoch:		2
License:	GPL
Group:		X11/Development/Tools
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_kdever}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	99dbd9bf9b2a1451544b35f73efe7dba
Source1:	%{name}-kommandersplash.png
Patch100:	%{name}-branch.diff
Patch0:		%{name}-quanta.patch
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1.6.1
BuildRequires:	kdelibs-devel >= %{_minlibsevr}
BuildRequires:	kdesdk-libcvsservice-devel >= 3:3.4.0
BuildRequires:	libgcrypt-devel
BuildRequires:	libxslt-devel >= 1.0.18
BuildRequires:	libxml2-devel >= 1:2.6.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	sed >= 4.0
#BuildRequires:	unsermake >= 040511
BuildConflicts:	quanta
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

%package kfilereplace
Summary:	A powerful string replacer
Summary(pl):	Rozbudowane narzêdzie do zamiany tekstu
Group:		X11/Development/Tools
Requires:	kdebase-core >= %{_minbasesevr}
Conflicts:	quanta < 1:3.2.90
Obsoletes:	kdesdk-kfilereplace

%description kfilereplace
KFileReplace is a KDE utility which replace some strings with others
in a lot of files in an only operation.

%description kfilereplace -l pl
KFileReplace to narzêdzie do masowej zmiany ró¿nych tekstów w du¿ej
ilo¶ci plików, podczas jednej operacji.

%package kimagemapeditor
Summary:	An HTML image map editor
Summary(pl):	Edytor map obrazów w HTML
Requires:	kdebase-core >= %{_minbasesevr}
Group:		X11/Development/Tools

%description kimagemapeditor
An HTML image map editor.

%description kimagemapeditor -l pl
Edytor map obrazów w HTML.

%package klinkstatus
Summary:	Link checker for KDE.
Summary(pl):	Program do sprawdzania odno¶ników pod KDE.
Requires:	kdebase-core >= %{_minbasesevr}
Group:		X11/Development/Tools
Conflicts:	kdewebdev-quanta_be

%description klinkstatus
KLinkStatus is an Open Source tool for checking links in a web page.
It can search by depth, domain or both. On a domain search it's also
possible to choose the search depth of URLs with foreign domain. For
performance, it supports several simultaneous connections and try to
use the same connection for the same sequence of requests.

%description klinkstatus -l pl
KLinkStatus jest narzêdziem do sprawdzania odno¶ników na stronie.
Obs³uguje wyszukiwanie wed³ug g³êboko¶ci, domeny lub obu naraz. W
wyszukiwaniu wed³ug domeny mo¿na równie¿ dodaæ maksymaln± g³êboko¶æ
dla pozosta³ych domen. Dla uzyskania jak najlepszej wydajno¶ci program
obs³uguje symultaniczne po³±czenia oraz próbuje wykorzystaæ jedno
po³±czenie dla wszystkich sekwencji ¿±dañ.

%package kommander
Summary:	A langauage independent visual dialog building tool
Summary(pl):	Niezale¿ne od jêzyka narzêdzie do budowy okien dialogowych
Group:		X11/Development/Tools
Requires:	kdebase-core >= %{_minbasesevr}
Conflicts:	quanta < 1:3.2.3

%description kommander
Kommander is a visual dialog building tool which may be expanded to
create full mainwindow applications. The primary objective is to
create as much functionality as possible without using any scripting
language. This is provided by the following features:
- Specials - these are prefaced with an "@" like @widgetText. They
  offer special features like the value of a widget, functions, aliases,
  global variables and such.
- DCOP integration - this allows Kommander dialogs to control and be
  controlled in interactions with other KDE applications.
- Signals and Slots - this is a little less intuitive to a new user.
  It is under review for how we process things in the first major
  release. These offer a limited event model for when a button is pushed
  or a widget is changed. Combined with "Population Text" it is rather
  powerful.

The central key feature of Kommander dialogs is that you can bind text
(Kommander Text) to a widget. So if you have @widget1 and @widget2 and
they are line edits you can set Kommander to show their contents by
entering @widgetText in their Kommander Text area. Then enter "hello"
in @widget1 and "world" in @widget2. A button can have the string "My
first @widget1 @widget2 program in Kommander". If you run this dialog
from a console it will output "My first hello world program in
Kommander".

Kommander also seeks to build on standards. It is built on the Qt
Designer framework and creates *.ui files which it renames to *.kmdr.
It can easily import any KDE widget and this can be done without
having to rebuild Kommander, by using plugins.

Kommander's other significant factor is being language neutral and
allowing a Kommander dialog to be extended by using any scripting
language. Kommander positions itself in a unique position for wide
spread adoption. Multiple script languages can be used in a single
dialog and applications can be taken over by people using a different
language than the original developer and gradually converting and
extending it. New widgets and features can be instantly leveraged by
all available languages.

%description kommander -l pl
Kommander to wizualne narzêdzie do tworzenia okien dialogowych, które
mo¿na rozszerzaæ o tworzenie pe³nych aplikacji z g³ównym oknem.
Podstawowym celem jest tworzenie jak najwiêkszej funkcjonalno¶ci bez
u¿ywania ¿adnego jêzyka skryptowego. Maj± to umo¿liwiæ nastêpuj±ce
cechy:
- specjalne oznaczenia - poprzedzone znakiem "@", jak @widgetText.
  Oferuj± one specjalne mo¿liwo¶ci, takie jak warto¶æ widgetu,
  funkcje, aliasy, zmienne globalne itp.
- integracja DCOP - umo¿liwia oknom Kommandera sterowanie i bycie
  sterowanym w interakcji z innymi aplikacjami KDE.
- Sygna³y i sloty - s± nieco mniej intuicyjne dla nowego u¿ytkownika.
  Jeszcze nie zosta³o ostatecznie ustalone, jak te rzeczy bêd±
  przetwarzane w pierwszym wydaniu. Oferuj± one ograniczony model
  zdarzeniowy dla sytuacji wci¶niêcia przycisku czy zmiany widgetu.
  W po³±czeniu z "Population Text" s± dosyæ potê¿nym narzêdziem.

Kluczow± cech± okien dialogowych Kommandera jest to, ¿e mo¿na
przywi±zaæ tekst (Kommander Text) do widgetu. Je¶li mamy @widget1 i
@widget2, i s± one liniami edycji, mo¿na ustawiæ Kommandera, by
pokazywa³ ich zawarto¶æ poprzez wpisanie @widgetText w ich polach
Kommander Text. Potem mo¿na wpisaæ "hello" w @widget1 i "world" w
@widget2. Przycisk mo¿e mieæ ³añcuch "Mój pierwszy program @widget1
@widget2 w Kommanderze". Je¶li uruchomimy to okno dialogowe z konsoli,
wypisze ono "Mój pierwszy program hello world w Kommanderze".

Kommander tak¿e usi³uje byæ oparty na standardach. Jest zbudowany na
¶rodowisku Qt Designera i tworzy pliki *.ui, którym zmienia nazwy na
*.kmdr. Mo¿e ³atwo zaimportowaæ dowolny widget KDE, co mo¿na ³atwo
zrobiæ poprzez u¿ycie wtyczek, bez potrzeby przebudowywania
Kommandera.

Kolejnym znacz±cym czynnikiem Kommandera jest bycie niezale¿nym od
jêzyka i mo¿liwo¶æ rozszerzania poprzez u¿ycie dowolnego jêzyka
skryptowego. Konqueror plasuje siê na unikalnej pozycji do szeroko
rozpowszechnionej adopcji. W jednym oknie dialogowym mo¿na u¿yæ wiele
jêzyków skryptowych, a aplikacje mog± byæ przejête przez ludzi
u¿ywaj±cych innego jêzyka ni¿ oryginalny twórca, a pó¼niej stopniowo
konwertowane i rozszerzane. Nowe widgety i mo¿liwo¶ci mog± byæ
natychmiast poddane wszystkim dostêpnym jêzykom.

%package kommander-devel
Summary:	Development files for kommander
Summary(pl):	Nag³ówki dla kommandera
Group:		X11/Development/Libraries
Requires:	%{name}-kommander = %{epoch}:%{version}-%{release}
Obsoletes:	quanta-devel
Provides:	quanta-devel = %{epoch}:%{version}-%{release}

%description kommander-devel
Development files for kommander.

%description kommander-devel -l pl
Nag³ówki dla kommandera.

%package kxsldbg
Summary:	KXsldbg - graphical debugger and frontend to xsldbg
Summary(pl):	KXsldbg - graficzny debugger i frontend do xsldbg
Group:		X11/Development/Tools
Requires:	kdebase-core >= %{_minbasesevr}
Conflicts:	quanta < 1:3.2.3

%description kxsldbg
KXsldbg is a graphical debugger and a frontend to xsldbg. It allows
to:
- set and modify breakpoints
- display value of expressions
- display information about breakpoints, templates, variables,
  callstack, stylesheets and entities found
- move around XSL source and XML document via XPaths
- lookup PUBLIC and SYSTEM ID's in the current XML catalog

%description kxsldbg -l pl
KXsldbg to graficzny debugger i frontend do xsldbg. Pozwana na:
- ustawianie i modyfikowanie pu³apek
- wy¶wietlanie warto¶ci wyra¿eñ
- wy¶wietlanie informacji o znalezionych pu³apkach, szablonach,
  zmiennych, stosie wywo³añ, arkuszach stylów i encjach
- przenoszenie ¼ród³a XSL i dokumentu XML poprzez XPaths
- wyszukiwanie identyfikatorów PUBLIC i SYSTEM w bie¿±cym katalogu XML

%package quanta
Summary:	Web development tool for KDE
Summary(es):	Uno editor WEB para KDE
Summary(pl):	Narzêdzie do tworzenia WWW dla KDE
Summary(pt_BR):	Um editor web para o KDE
Group:		X11/Development/Tools
Requires:	kdebase-core >= %{_minbasesevr}
# Applications required for full functionality:
%if 0
Requires:	kdesdk-kompare
Requires:	kdewebdev-kfilereplace
Requires:	kdewebdev-kommander
Requires:	kdewebdev-kxsldbg
Requires:	kdewebdev-kimagemapeditor
Requires:	kdewebdev-klinkstatus
%endif
Obsoletes:	kdewebdev-quanta_be
Obsoletes:	quanta
Obsoletes:	quanta-doc
# until some packets provide these:
Obsoletes:	quanta-doc-css
Obsoletes:	quanta-doc-html
Obsoletes:	quanta-doc-javascript
Obsoletes:	quanta-doc-php

%description quanta
Quanta Plus is a web development tool for the K Desktop Environment.
Quanta is designed for quick web development and is rapidly becoming a
mature editor with a number of great features.

%description quanta -l es
Quanta Plus és una herramienta de desarrollo web para KDE. Es
projetado para rapido desarrollo web e es casi pronto com excelent
quantidad de caracteristicas.

%description quanta -l pl
Quanta Plus to narzêdzie do tworzenia WWW dla ¶rodowiska KDE. S³u¿y do
szybkiego tworzenia stron i staje siê dojrza³ym edytorem z wieloma
przydatnymi mo¿liwo¶ciami.

%description quanta -l pt_BR
O Quanta Plus é uma ferramenta para desenvolvimento web para o KDE. É
projetado para desenvolvimento web rápido e está rapidamente se
tornando um editor maduro com um bom número de excelentes
características.

%prep
%setup -q
#%patch100 -p1
%patch0 -p1
install %{SOURCE1} kommander/editor/pics/kommandersplash.png

%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Development;WebDevelopment;/' \
	./kimagemapeditor/kimagemapeditor.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Development;WebDevelopment;/' \
	./klinkstatus/src/klinkstatus.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Development;WebDevelopment;/' \
	./kommander/editor/kmdr-editor.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Development;WebDevelopment;/' \
	./kxsldbg/kxsldbg.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Development;WebDevelopment;/' \
	quanta/src/quanta.desktop

%build
cp -f /usr/share/automake/config.sub admin

#export UNSERMAKE=/usr/share/unsermake/unsermake

%{__make} -f admin/Makefile.common cvs

%configure \
	--disable-rpath \
	--enable-final \
	--enable-editors \
	--with-qt-libraries=%{_libdir} \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

# Debian manpages
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install debian/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

%find_lang kfilereplace	--with-kde
%find_lang klinkstatus	--with-kde
%find_lang kommander	--with-kde
%find_lang kxsldbg	--with-kde
%find_lang quanta	--with-kde
%find_lang xsldbg	--with-kde
cat xsldbg.lang >> kxsldbg.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post	kommander	-p /sbin/ldconfig
%postun	kommander	-p /sbin/ldconfig

%files kfilereplace -f kfilereplace.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kfilereplace
%{_libdir}/kde3/libkfilereplacepart.la
%attr(755,root,root) %{_libdir}/kde3/libkfilereplacepart.so
%{_datadir}/apps/kfilereplace
%{_datadir}/apps/kfilereplacepart
%{_datadir}/services/kfilereplacepart.desktop
%{_desktopdir}/kde/kfilereplace.desktop
%{_iconsdir}/[!l]*/*/apps/kfilereplace.png

%files kimagemapeditor
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kimagemapeditor
%{_libdir}/kde3/libkimagemapeditor.la
%attr(755,root,root) %{_libdir}/kde3/libkimagemapeditor.so
%{_datadir}/apps/kimagemapeditor
%{_datadir}/services/kimagemapeditorpart.desktop
%{_desktopdir}/kde/kimagemapeditor.desktop
%{_iconsdir}/[!l]*/*/apps/kimagemapeditor.png
%{_mandir}/man1/kimagemapeditor.1*

%files klinkstatus -f klinkstatus.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/klinkstatus
%{_libdir}/kde3/libklinkstatuspart.la
%attr(755,root,root) %{_libdir}/kde3/libklinkstatuspart.so
%{_datadir}/apps/klinkstatuspart/pics/304.png
%{_datadir}/apps/klinkstatus/klinkstatus_shell.rc
%{_datadir}/apps/klinkstatuspart/klinkstatus_part.rc
%{_datadir}/config.kcfg/klinkstatus.kcfg
%{_datadir}/services/klinkstatus_part.desktop
%{_desktopdir}/kde/klinkstatus.desktop
%{_iconsdir}/hicolor/*/apps/klinkstatus.png
%{_mandir}/man1/klinkstatus.1*

%files kommander -f kommander.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmdr-editor
%attr(755,root,root) %{_bindir}/kmdr-executor
%attr(755,root,root) %{_bindir}/kmdr-plugins
%{_libdir}/libkommanderplugin.la
%attr(755,root,root) %{_libdir}/libkommanderplugin.so.*.*.*
%{_libdir}/libkommanderwidget.la
%attr(755,root,root) %{_libdir}/libkommanderwidget.so.*.*.*
%{_libdir}/libkommanderwidgets.la
%attr(755,root,root) %{_libdir}/libkommanderwidgets.so.*.*.*
%{_datadir}/applnk/.hidden/kmdr-executor.desktop
%{_datadir}/mimelnk/application/x-kommander.desktop
%{_datadir}/apps/kmdr-editor/pics/kommandersplash.png
%{_desktopdir}/kde/kmdr-editor.desktop
%{_mandir}/man1/kmdr-editor.1*
%{_mandir}/man1/kmdr-executor.1*
%{_mandir}/man1/kmdr-plugins.1*

%files kommander-devel
%defattr(644,root,root,755)
%{_libdir}/libkommanderplugin.so
%{_libdir}/libkommanderwidget.so
%{_libdir}/libkommanderwidgets.so
%{_includedir}/kommanderfactory.h
%{_includedir}/kommanderplugin.h
%{_includedir}/kommanderwidget.h

%files kxsldbg -f kxsldbg.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kxsldbg
%attr(755,root,root) %{_bindir}/xsldbg
%{_libdir}/kde3/libkxsldbgpart.la
%attr(755,root,root) %{_libdir}/kde3/libkxsldbgpart.so
%{_datadir}/apps/kxsldbg
%{_datadir}/apps/kxsldbgpart
%{_datadir}/services/kxsldbg_part.desktop
%{_desktopdir}/kde/kxsldbg.desktop
%{_iconsdir}/[!l]*/*/actions/xsldbg_*.png
%{_mandir}/man1/kxsldbg.1*

%files quanta -f quanta.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/quanta
%{_libdir}/kde3/quantadebuggergubed.la
%attr(755,root,root) %{_libdir}/kde3/quantadebuggergubed.so
%{_datadir}/apps/kafkapart
%{_datadir}/apps/quanta
%{_datadir}/apps/templates
%{_datadir}/mimelnk/application/x-webprj.desktop
%{_datadir}/services/quanta_preview_config.desktop
%{_datadir}/services/quantadebuggergubed.desktop
%{_datadir}/servicetypes/quantadebugger.desktop
%{_desktopdir}/kde/quanta.desktop
%{_iconsdir}/[!l]*/*/apps/quanta.png
%{_iconsdir}/[!l]*/*/actions/[!x]*.png
%{_mandir}/man1/quanta.1*
