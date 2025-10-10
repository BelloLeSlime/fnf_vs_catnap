function onEvent(name, value1, value2)
    if name == 'altsubtitties' then
        fade = 0
        setTextString('subtitle', value1)
        setTextColor('subtitle', value2)
        runTimer('subtitlefade', 2, 1)
    end
end

function onCreate()
    fade = 0
    makeLuaText('subtitle', '', 400, 435, 300)
    addLuaText('subtitle')
    setObjectCamera('subtitle', 'other');
    setTextSize('subtitle', 50)
end

function onUpdate()
    fade = fade + 1
    if fade > 300 then
        setTextString('subtitle', '')
    end
end