import pygame as pg
import OpenGL.GL as glmod
pg.init()

triangle_vertices = (
(0,1),(-1,-1),(1,-1)
    )
vertices_color = (
(1,0,0),(0,1,0),(0,0,1)
    )

class Game(object):
    def __init__(self,dims,title,framerate):
        pg.display.set_caption(title)
        flags = pg.OPENGL|pg.DOUBLEBUF
        bpp = pg.display.mode_ok(dims,flags)
        self.win = pg.display.set_mode(dims,flags,bpp)
        self.clk = pg.time.Clock()
        self.fps = framerate
        self.done = False
        glmod.glEnable(glmod.GL_DEPTH_TEST)
        glmod.glDepthFunc(glmod.GL_LESS)
    def run(self):
        self._mainloop()
    def _process_events(self):
        for e in pg.event.get():
            if e.type in (pg.QUIT, pg.WINDOWCLOSE):
                self.done = True
                return
    def _process_drawing(self):
        glmod.glClear(glmod.GL_COLOR_BUFFER_BIT|glmod.GL_DEPTH_BUFFER_BIT|glmod.GL_STENCIL_BUFFER_BIT)
        glmod.glClearColor(.1,.1,.1,1)
        ##draw a basic triangle with 3 vertex datas
        glmod.glBegin(glmod.GL_TRIANGLES)
        for i in range(len(triangle_vertices)):
            glmod.glColor3f(*vertices_color[i])
            glmod.glVertex2f(*triangle_vertices[i])
        glmod.glEnd()
        
        pg.display.flip()  ##update everything you've drawn
    def _process_game_logic(self): pass
    def _mainloop(self):
        while not self.done:
            self._process_events()
            self._process_drawing()
            self._process_game_logic()
            self.clk.tick(self.fps)
        pg.quit()

def main():
    FPS = 60
    WINW = 640
    WINH = 480
    DIMS = WINW,WINH
    TITLE = 'pyopengl application running'
    Game(DIMS,TITLE,FPS).run()

if __name__ == '__main__':
    main()
