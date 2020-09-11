uniform mat4 u_MVPMatrix;    //变换矩阵
uniform float u_AnimationFraction;  //动画进度
attribute vec4 a_Position;   //顶点坐标
attribute vec2 a_TexCoordinate; //纹理坐标

varying vec2 v_TexCoordinate;


void main() 
{
   //传递纹理坐标的值到纹理着色器
   v_TexCoordinate = a_TexCoordinate;
   
   vec4 finalPosition = a_Position;
   
   //制造一个随机漂移值
   float randomValue = (sin(u_AnimationFraction)) * (finalPosition.z - 0.5) * 0.2; 
   //碎片随机左移或者右移
   finalPosition.x = finalPosition.x + randomValue * 0.2;
   //碎片随机加速
   finalPosition.y = finalPosition.y - u_AnimationFraction - finalPosition.z * 0.2 * u_AnimationFraction;
   finalPosition.z = finalPosition.z * (u_AnimationFraction / 2.0) * 0.1;
   
   gl_Position = u_MVPMatrix * finalPosition;
}