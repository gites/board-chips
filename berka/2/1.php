<?php

$font = imageloadfont('./arial.gdf');
$im = imagecreatefrompng("T59-maly1.png");
$textcolor = imagecolorallocate($im, 0, 0, 0);
//nazwa jednostki (a co z kwadracikiem?)
imagestring($im, 1, 3, 3, '509', $textcolor);
//sila
imagestring($im, 3, 20, 34, '5-6', $textcolor);
//ruch
//imagestring($im, 2, 35, 34, '6', $textcolor);
//gwiazdki 1
imagestringup($im, 1, 3, 30, 'XXX', $textcolor);
//gwiazdki 2
imagestring($im, 1, 3, 34, '##', $textcolor);
imagestring($im, 1, 3, 40, '++', $textcolor);

imagepng($im,"2.png");
?>
