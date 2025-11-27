#### **Příprava lokálního repozitáře**

Inicializace lokal repo ... v aktuální složce
> *git init

Informace o stavu repozitáře proti aktuální větvi
> *git status

Přejmenování main větve podle GitHub (ve výchozím stavu se jmenuje  *origin* )
> *git branch -M main

Připojení remote repo na GitHub
> *git remote add origin https://github.com/MaxxShadow/test_git_project.git

#### **Uložení změn do remote repo**

> *git add \<soubor\>

... nebo hromadně
> *git add \*

> *git commit -m "Pocatecni commit"
> git commit -m \<mesydž\>   ... např. "commit.251005.1640"
> git push -u origin main

... později stačí
> *git push

#### **Stažení změn z remote repozitory**

Načtení všech změn
> *git fetch

Stažení změn
> *git pull


#### **Práce s novou větví**

Příprava čisté lokální repozitory  na aktuální `main` , tj. stažení aktuálního stavu z repozitáře
> *git checkout main
> git pull

Vytvoření si vlastní pracovní větve `feature-moje-zmeny`
> *git checkout -b feature-moje-zmeny

Vlastní vývoj v nové větvi `feature-moje-zmeny`, tj. změny mimo `main`
> *git add *
> git commit -m "Rozpracované úpravy"
> git push -u origin feature-moje-zmeny

Merging změny do `main`
> *git checkout main
> git merge feature-moje-zmeny
> git push

Obnova čisté produkční verze bez vývojových změn
> *git checkout main
> git pull

