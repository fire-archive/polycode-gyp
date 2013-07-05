{
  'conditions': [
    ['OS=="win"', {
      'targets': [
        {
          'target_name': 'wglext_download',
          'type': 'none',
          'msvs_cygwin_shell': '0',
          'actions': [
            {
              'action_name': 'downloading wglext.h...',
              'inputs': [ '../third_party/glext/dummy.txt' ],
              'outputs': [ 'wglext.h' ],
              'action': ['powershell', "(New-Object System.Net.WebClient).DownloadFileAsync('https://www.opengl.org/registry/api/glext.h', '../third_party/glext/GL/wglext.h')"]
            },
          ],
        },
      ]
        }, { # OS != "win"
       'targets': [
       {
         'target_name': 'glext_download',
         'type': 'none',
         'actions': [
         {
           'action_name': 'downloading wglext.h...',
           'inputs': [ '../third_party/glext/dummy.txt' ],
           'outputs': [ 'wglext.h' ],
           'action': [ 'curl', '-o', '../third_party/glext/GL/wglext.h', 'https://www.opengl.org/registry/api/wglext.h' ],
		     }, ],
      }, ],  
    }, ], ],
}
