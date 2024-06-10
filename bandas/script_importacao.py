import os
import json

from django.db import transaction
from bandas.models import Banda, Album, Musica

def importar_bandas(archive_name):
    try:
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(diretorio_atual, archive_name)

        with open(path, 'r') as f:
            data = json.load(f)

            with transaction.atomic():
                for banda_data in data['bandas']:
                    banda, created = Banda.objects.get_or_create(
                        name=banda_data['name'],
                        defaults={'image': banda_data['image'], 'foundation': banda_data['foundation']}
                    )

                    for album_data in banda_data['albums']:
                        album, created = Album.objects.get_or_create(
                            name=album_data['name'],
                            banda=banda,
                            defaults={'image': album_data['image'], 'dataDeCriacao': album_data['dataDeCriacao']}
                        )

                        for musica_data in banda_data['musics']:
                            Musica.objects.get_or_create(
                                name=musica_data['name'],
                                album=album,
                                defaults={'spotify_link': musica_data['spotify_link']}
                            )

        print("Importação completa")
    except Exception as e:
        print(f"Erro: {e}")