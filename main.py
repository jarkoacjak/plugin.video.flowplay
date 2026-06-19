# -*- coding: utf-8 -*-
import sys
import urllib.parse
import xbmcgui
import xbmcplugin

def build_url(query):
    return sys.argv[0] + '?' + urllib.parse.urlencode(query)

def main():
    handle = int(sys.argv[1])
    arg_string = sys.argv[2][1:] if len(sys.argv[2]) > 1 else ""
    params = dict(urllib.parse.parse_qsl(arg_string))

    mode = params.get('mode')
    action = params.get('action')

    # --- ŠPECIÁLNA AKCIA PRE BAMBUĽKU 3 (Vyskakovacie okno) ---
    if action == 'bambulka3_oznam':
        dialog = xbmcgui.Dialog()
        dialog.notification('Bambuľka 3', 'Ešte sme nevysielali alebo neni pridane', xbmcgui.NOTIFICATION_INFO, 5000)
        return

    # --- HLAVNÉ MENU ---
    if not mode:
        categories = [
            {"label": "Relácie", "mode": "relacie"},
            {"label": "Filmy", "mode": "filmy"},
            {"label": "Deti", "mode": "deti"}
        ]

        for kat in categories:
            li = xbmcgui.ListItem(label="[B]" + kat["label"] + "[/B]")
            url = build_url({'mode': kat['mode']})
            xbmcplugin.addDirectoryItem(handle, url, li, True)
        
        xbmcplugin.endOfDirectory(handle)

    # --- SEKCIA RELÁCIE (Logistika s automatickou upútavkou) ---
    elif mode == 'relacie':
        video_id = "_oFCqhIa9Ls"
        url = "plugin://plugin.video.youtube/play/?video_id=" + video_id
        
        li = xbmcgui.ListItem(label="Logistika")
        li.setInfo('video', {
            'title': 'Logistika', 
            'plot': 'Pripravujeme čoskoro... Po kliknutí sa spustí upútavka.'
        })
        li.setProperty('IsPlayable', 'true')
        
        xbmcplugin.addDirectoryItem(handle, url, li, False)
        xbmcplugin.endOfDirectory(handle)

    # --- SEKCIA DETI (Bambuľka) ---
    elif mode == 'deti':
        # 1. a 2. epizóda
        episody = [
            {"label": "Bambuľka 1", "id": "UOCo8fLEoUo"},
            {"label": "Bambuľka 2", "id": "674vZJ_t4WA"},
        ]

        for ep in episody:
            li = xbmcgui.ListItem(label=ep["label"])
            url = "plugin://plugin.video.youtube/play/?video_id=" + ep["id"]
            li.setProperty('IsPlayable', 'true')
            xbmcplugin.addDirectoryItem(handle, url, li, False)
            
        # 3. epizóda - Po kliknutí spustí akciu s oznamom hore v rohu obrazovky
        li3 = xbmcgui.ListItem(label="Bambuľka 3")
        li3.setInfo('video', {
            'title': 'Bambuľka 3',
            'plot': 'Ešte sme nevysielali alebo neni pridane.'
        })
        url3 = build_url({'action': 'bambulka3_oznam'})
        xbmcplugin.addDirectoryItem(handle, url3, li3, False)
            
        xbmcplugin.endOfDirectory(handle)

    # --- SEKCIA FILMY ---
    elif mode == 'filmy':
        li = xbmcgui.ListItem(label="[I]Filmy - Už čoskoro...[/I]")
        # Musíme poslať aspoň základné kormidlo, aby Kodi vedelo kliknúť bez pádu
        url_placeholder = build_url({'mode': 'filmy'})
        xbmcplugin.addDirectoryItem(handle, url_placeholder, li, False)
        xbmcplugin.endOfDirectory(handle)

if __name__ == '__main__':
    main()
