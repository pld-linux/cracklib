Summary:	Password checking library
Summary(es):	Biblioteca de chequeo de contraseЯas
Summary(fr):	BibliothХque de vИrification de mots de passe
Summary(pl):	Biblioteka sprawdzania haseЁ
Summary(pt_BR):	Biblioteca de checagem de senhas
Summary(ru):	Библиотека проверки паролей
Summary(tr):	Parola denetim kitaplЩПЩ
Summary(uk):	Б╕бл╕отека перев╕рки парол╕в
Name:		cracklib
Version:	2.7
Release:	17
License:	Artistic
Group:		Libraries
Source0:	ftp://coast.cs.purdue.edu/pub/tools/unix/libs/cracklib/%{name}_%{version}.tgz
# Source0-md5: 7f810e310c7f2df33d1eaa2b41ab2435
Patch0:		%{name}.patch
Patch1:		%{name}-pld.patch
Patch2:		%{name}-nss.patch
Patch3:		%{name}-libdir.patch
BuildRequires:	words
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CrackLib tests passwords to determine whether they match certain
security-oriented characteristics. You can use CrackLib to stop users
from choosing passwords which would be easy to guess. CrackLib
performs certain tests:

- It tries to generate words from a username and gecos entry and
  checks those words against the password;
- It checks for simplistic patterns in passwords;
- It checks for the password in a dictionary.

CrackLib is actually a library containing a particular C function
which is used to check the password, as well as other C functions.
CrackLib is not a replacement for a passwd program; it must be used in
conjunction with an existing passwd program.

Install the cracklib package if you need a program to check users'
passwords to see if they are at least minimally secure. If you install
CrackLib, you'll also want to install the cracklib-dicts package.

%description -l de
эberprЭft PaъwЖrter auf Sicherheitsmerkmale - LДnge, Eindeutigkeit,
Anwesenheit in einer WЖrter-Datenbank usw.

%description -l es
Incluye los diccionarios cracklib para el padrСn /usr/dict/words, asМ
como, los utilitarios necesarios para crear diccionarios.

%description -l fr
VИrifie les caractИristiques liИes Ю la sИcuritИ des mots de passe -
longueur, unicitИ, s'ils sont dans une base de mots, etc.

%description -l pl
Sprawdza hasЁa pod k╠tem bezpieczeЯstwa - dЁugo╤Ф, unikalno╤Ф, czy
wystЙpuj╠ w sЁowniu itp.

%description -l pt_BR
Inclui os dicionАrios cracklib para o padrЦo /usr/dict/words, assim
como os utilitАrios necessАrios para criar dicionАrios.

%description -l ru
CrackLib проверяет пароли на предмет соответствия некоторым критериям
безопасности. Она может быть использована для предотвращения выбора
пользователями легкоугадываемых паролей. CrackLib производит такие
тесты:

- Генерирует слова из имени пользователя и поля gecos и сравнивает их
  с паролем;
- Ищет в паролях простые шаблоны;
- Проверяет пароль на наличие его в словаре.

CrackLib - это, собственно, библиотека, содержащая специфическую
функцию C для угадывания паролей и некоторые другие функции. Это не
замена программы passwd, ее надо использовать совместно с существующей
программой passwd.

%description -l tr
ParolalarЩn uzunluklarЩ, sistemde tek olmalarЩ, sЖzcЭk veri tabanЩnda
bulunmamalarЩ gibi gЭvenlikle ilgili Жzelliklerini kontrol eder.

%description -l uk
CrackLib перев╕ря╓ парол╕ на в╕дпов╕дн╕сть деяким критер╕ям безпеки.
Вона може бути використана для запоб╕гання вибору користувачами
парол╕в, як╕ легко в╕дгадати. Вона викону╓ так╕ тести:

- Генеру╓ слова з ╕мен╕ користувача та поля gecos ╕ пор╕вню╓ ╖х з
  паролем;
- Шука╓ в паролях прост╕ шаблони;
- Перев╕ря╓ парол╕ на наявн╕сть ╖х у словнику.

CrackLib - це, власне, б╕бл╕отека, що м╕стить специф╕чну функц╕ю C для
в╕дгадування парол╕в та деяк╕ ╕нш╕ функц╕╖. Це не зам╕на програми
passwd, ╖╖ треба використовувати сп╕льно з ╕снуючою програмою passwd.

%package devel
Summary:	Header files and documentation for cracklib
Summary(es):	Archivos de inclusiСn y bibliotecas para cracklib
Summary(pl):	Pliki nagЁСwkowe i dokumentacja dla cracklib
Summary(pt_BR):	Arquivos de inclusЦo e bibliotecas para a cracklib
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files and documentation for cracklib.

%description devel -l es
Este paquete contiene los archivos de inclusiСn y bibliotecas que se
necesitan para desarrollar programas que usan cracklib.

%description devel -l pl
Pliki nagЁСwkowe i dokumentacja dla cracklib.

%description devel -l pt_BR
Este pacote contИm os arquivos de inclusЦo e bibliotecas que sЦo
necessАrios para desenvolver programas que usam a cracklib.

%package dicts
Summary:	Standard dictionaries (/usr/share/dict/words)
Summary(de):	Standard-WЖrterbЭcher (/usr/share/dict/words)
Summary(es):	Diccionarios para chequeo de contraseЯas
Summary(fr):	Dictionnaires standards (/usr/share/dict/words)
Summary(pl):	Standardowe sЁowniki (/usr/share/dict/words)
Summary(pt_BR):	DicionАrios para checagem de senhas
Summary(ru):	Стандартные словари CrackLib
Summary(tr):	Standart sЖzlЭkler (/usr/share/dict/words)
Summary(uk):	Стандартн╕ словники CrackLib
Group:		Applications/System

%description dicts
The cracklib-dicts package includes the CrackLib dictionaries.
CrackLib will need to use the dictionary appropriate to your system,
which is normally put in /usr/share/dict/words. Cracklib-dicts also
contains the utilities necessary for the creation of new dictionaries.

%description dicts -l de
EnthДlt die Cracklib-WЖrterbЭcher fЭr die
Standard-/usr/share/dict/WЖrter sowie Utilities zum Erstellen neuer
WЖrterbЭcher"

%description dicts -l es
Incluye el diccionario cracklib para el padrСn /usr/dict/words, bien
como utilitarios necesarios a creaciСn de nuevos diccionarios.

%description dicts -l fr
Contient les dictionnaires cracklib pour le /usr/share/dict/words
standard, ainsi que les utilitaires nИcessaires Ю la crИation de
nouveaux dictionnaires.

%description dicts -l pl
Pakiet zawiera sЁowniki cracklib'a dla standardowego
/usr/share/dict/words oraz narzЙdzia do tworzenia nowych sЁownikСw.

%description dicts -l pt_BR
Inclui o dicionАrio cracklib para o padrЦo /usr/dict/words, bem como
utilitАrios necessАrios a criaГЦo de novos dicionАrios.

%description dicts -l ru
Пакет cracklib-dicts включает словари CrackLib. CrackLib будут нужны
словари, соответствующие вашей системе, которые обычно находятся в
/usr/share/dict/words. Cracklib-dicts также содержит утилиты,
необходимые для создания новых словарей.

%description dicts -l tr
/usr/share/dict/words dosyasЩ iГin 'cracklib' kitaplЩklarЩnЩ ve yeni
sЖzlЭkler yaratЩlmasЩ iГin gerekli yardЩmcЩ programlarЩ iГerir.

%description dicts -l uk
Пакет cracklib-dicts м╕стить словники CrackLib. CrackLib будуть
потр╕бн╕ словники, що в╕дпов╕дають ваш╕й систем╕, котр╕ зазвичай
знаходяться в /usr/share/dict/words. Cracklib-dicts також м╕стить
утил╕ти, необх╕дн╕ для створення нових словник╕в.

%prep
%setup	-q -n %{name},%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__make} all \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_libdir},%{_includedir},%{_datadir}/dict}

%{__make} install \
	libdir=%{_libdir} \
	ROOT=$RPM_BUILD_ROOT

install cracklib/packer.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README MANIFEST LICENCE POSTER HISTORY

%attr(755,root,root) %{_libdir}/lib*so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*

%files dicts
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
%{_datadir}/dict/cracklib_dict*
