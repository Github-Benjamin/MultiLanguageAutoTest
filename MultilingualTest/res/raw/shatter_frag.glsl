precision mediump float;       	
uniform sampler2D u_Texture;
varying vec2 v_TexCoordinate;

void main()
{
    //根据纹理坐标以及纹理取样器来设置片元色
    gl_FragColor = texture2D(u_Texture, v_TexCoordinate);
}
