{
  'conditions': [
    ['OS=="win"', {
      'targets': [
        {
          'target_name': 'glext_download',
          'type': 'none',
          'msvs_cygwin_shell': '0',
          'actions': [
            {
              'action_name': 'downloading glext.h...',
              'inputs': [ '../third_party/glext/dummy.txt' ],
              'outputs': [ 'glext.h' ],
              'action': ['powershell', "(New-Object System.Net.WebClient).DownloadFile(\"http://www.opengl.org/registry/api/glext.h\", '../third_party/glext/GL/glext.h\')"]
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
           'action_name': 'downloading glext.h...',
           'inputs': [ '../third_party/glext/dummy.txt' ],
           'outputs': [ 'glext.h' ],
           'action': [ 'curl', '-o', '../third_party/glext/GL/glext.h', 'https://www.opengl.org/registry/api/glext.h' ],
		     }, ],
      }, ],  
    }, ], ],
}
