
function onCreate()
	-- background shit
	makeLuaSprite('altrejectwall', 'altrejectwall', -300, -350);
	setScrollFactor('altrejectwall', 0.9, 0.9);
	scaleObject('altrejectwall', 1.5, 1.5);
	
	makeLuaSprite('altrejectfloor', 'altrejectfloor', -950, 150);
	setScrollFactor('altrejectfloor', 0.9, 0.9);
	scaleObject('altrejectfloor', 2.7, 2.7);



	addLuaSprite('altrejectwall', false);
	addLuaSprite('altrejectfloor', false);
end