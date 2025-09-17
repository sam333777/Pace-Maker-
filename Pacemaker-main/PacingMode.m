classdef PacingMode < Simulink.IntEnumType
    methods (Static = true)
        function retVal = addClassNameToEnumNames()
            retVal = true;
        end
    end

    enumeration
        VVI(0)
        AAI(1)
        VOO(2)
        AOO(3)
    end
    

end
