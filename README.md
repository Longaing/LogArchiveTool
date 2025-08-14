# Outil d'Archive de Journaux (Log Archiver)

Un script Python pour archiver automatiquement les fichiers journaux dans une archive compressée avec horodatage.

## 📝 Description

Cet outil permet de :
- Archiver tous les fichiers d'un dossier de logs spécifié
- Créer une archive compressée au format `.tar.gz`
- Nommer automatiquement l'archive avec la date et l'heure
- Stocker les archives dans un sous-dossier dédié
- Maintenir un système propre en organisant les anciens journaux

## 📥 Installation

1. **Prérequis** :
   - Python 3.6 ou supérieur
   - Accès en lecture sur le dossier de logs
   - Accès en écriture pour créer les archives

2. **Téléchargement** :
   ```
    git clone https://github.com/Longaing/LogArchiveTool.git
    cd log-archiver
    ```

3. **Exécution**

    Création d'un sous-dossier archive

    ```
    python3 log_archiver.py /var/log
    ```

puis exécution 

```
    python3 log_archiver.py test_logs
```