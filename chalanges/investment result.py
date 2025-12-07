capital = 5000
rateOfInterest = 0.08
inflationRate = 0.15 
zwrotInwestycji = capital * rateOfInterest; print(zwrotInwestycji)
wartoscPoInflacji = capital*inflationRate; print(wartoscPoInflacji)

capital += zwrotInwestycji
capital -= wartoscPoInflacji
print(capital)