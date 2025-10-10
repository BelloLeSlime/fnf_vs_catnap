function onCreate()
    if getPropertyFromClass('ClientPrefs', 'pauseMusic') ~= 'dogday_pause' then
        setPropertyFromClass('PauseSubState', 'songName', 'dogday_pause')
    end
end