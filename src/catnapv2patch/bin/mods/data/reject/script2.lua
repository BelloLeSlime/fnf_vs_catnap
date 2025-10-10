function opponentNoteHit()
    health = getProperty('health')
    if getProperty('health') > 0.045 then
        setProperty('health', health- 0.019);
    end
end