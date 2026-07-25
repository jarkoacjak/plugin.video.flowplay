```python
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

    # ---------------- OZNAM PRE NEDOSTUPNÉ EPIZÓDY ----------------
    if action == 'oznam':
        dialog = xbmcgui.Dialog()
        dialog.notification(
            'Informácia',
            'Ešte sme nevysielali alebo nie je pridané.',
            xbmcgui.NOTIFICATION_INFO,
            5000
        )
        return

    # ---------------- HLAVNÉ MENU ----------------
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

    # ---------------- RELÁCIE ----------------
    elif mode == "relacie":

        li = xbmcgui.ListItem(label="Logistika")
        url = build_url({'mode': 'logistika'})
        xbmcplugin.addDirectoryItem(handle, url, li, True)

        xbmcplugin.endOfDirectory(handle)

    # ---------------- LOGISTIKA ----------------
    elif mode == "logistika":

        li = xbmcgui.ListItem(label="1. séria")
        url = build_url({'mode': 'logistika_s1'})
        xbmcplugin.addDirectoryItem(handle, url, li, True)

        xbmcplugin.endOfDirectory(handle)

    # ---------------- LOGISTIKA 1. SÉRIA ----------------
    elif mode == "logistika_s1":

        epizody = [
            {
                "label": "1. epizóda",
                "id": "JLftU2_Metg"
            }
        ]

        for ep in epizody:
            li = xbmcgui.ListItem(label=ep["label"])
            li.setProperty('IsPlayable', 'true')

            url = "plugin://plugin.video.youtube/play/?video_id=" + ep["id"]

            xbmcplugin.addDirectoryItem(handle, url, li, False)

        xbmcplugin.endOfDirectory(handle)

    # ---------------- DETI ----------------
    elif mode == "deti":

        episody = [
            {"label": "Bambuľka 1", "id": "UOCo8fLEoUo"},
            {"label": "Bambuľka 2", "id": "674vZJ_t4WA"},
            {"label": "Bambuľka 3", "id": ""},
            {"label": "Bambuľka 4", "id": ""},
            {"label": "Bambuľka 5", "id": ""},
            {"label": "Bambuľka 6", "id": ""},
        ]

        for ep in episody:

            li = xbmcgui.ListItem(label=ep["label"])

            if ep["id"]:

                url = "plugin://plugin.video.youtube/play/?video_id=" + ep["id"]
                li.setProperty('IsPlayable', 'true')

            else:

                li.setInfo('video', {
                    'title': ep["label"],
                    'plot': 'Ešte sme nevysielali alebo nie je pridané.'
                })

                url = build_url({'action': 'oznam'})

            xbmcplugin.addDirectoryItem(handle, url, li, False)

        xbmcplugin.endOfDirectory(handle)

    # ---------------- FILMY ----------------
    elif mode == "filmy":

        li = xbmcgui.ListItem(label="[I]Filmy - Už čoskoro...[/I]")
        url = build_url({'action': 'oznam'})
        xbmcplugin.addDirectoryItem(handle, url, li, False)

        xbmcplugin.endOfDirectory(handle)


if __name__ == '__main__':
    main()
```
