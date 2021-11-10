import os



class PATH ():

    dire = os.path.dirname(os.path.abspath( __file__ ))
    # 상위 디렉토리
    par_dir = os.path.abspath(os.path.join(dire, os.pardir))
    
    par_dir = os.path.abspath(os.path.join(par_dir, os.pardir))

    data_dir = par_dir + '/data'

    html_dir = par_dir + '/html'

    map_html = html_dir + "/map.html"