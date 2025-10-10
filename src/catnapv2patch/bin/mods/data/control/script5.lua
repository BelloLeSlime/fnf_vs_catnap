function onBeatHit()
    if curBeat == 32 then
    doTweenAlpha('blackout', 'blackout', 0, 8, 'linear') 
end
end

function onCreate()
makeLuaSprite('blackout', 'blackout', -700, -400);
scaleObject('blackout', 5, 5);
addLuaSprite('blackout', true);
end