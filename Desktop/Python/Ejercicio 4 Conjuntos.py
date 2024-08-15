def departamentos() :
    dep = {"Artigas", "Canelones", "Cerro Largo", "Colonia", "Durazno", "Flores", "Florida", "Lavalleja", "Maldonado", "Montevideo", "Paysandú", "Río Negro", "Rivera", "Rocha", "Salto", "San José", "Soriano", "Tacuarembó", "Treinta y Tres"}
    dep_fronterisos = {"Salto","Artigas","Rivera","Tacuarembó","Cerro Largo","Soriano","Paysandú","Colonia"}
    dep_serranos = {"Maldonado", "Lavalleja", "Rocha", "Treinta y Tres", "Cerro Largo"} 
    dep_playas = {"Maldonado", "Rocha"}
    dep_no_fronterisos = dep-dep_fronterisos
    dep_no_fron_ni_sierra = dep_no_fronterisos-dep_serranos
    dep_turista = dep_serranos & dep_playas
    dep_malisimo = dep - dep_turista
    print(dep_no_fronterisos)
    print(dep_no_fron_ni_sierra)
    print(dep_turista)
    print(dep_malisimo)
departamentos()
