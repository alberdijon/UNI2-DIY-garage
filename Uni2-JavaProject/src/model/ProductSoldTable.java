/*
 * This software has been developed by Uni2
 * Under the GNU General Public License
 */
package model;

import java.util.ArrayList;

/**
 *
 * @author rodriguez.markel
 */
public class ProductSoldTable {
       private ArrayList<ProductSold> productos = new ArrayList<>();
    private String[] columns = {"Client-DNI, Product-ID, Amount, Date, Hour, Total_price"};

     public ProductSoldTable(ArrayList<ProductSold> products){
        this.productos = products;
     
    }
     
    public int getRowCount() {
        return productos.size();
    }

    public int getColumnCount() {
        return columns.length;
    }
   
    public String getColumnName(int column){
        return columns[column];
    }
   
    public Object getValueAt(int rowIndex, int columnIndex) {
       switch(columnIndex){
            case 0: return productos.get(rowIndex).getId();
            case 1: return productos.get(rowIndex).getName();
            case 2: return productos.get(rowIndex).getPrice();
            case 3: return productos.get(rowIndex).getStock();
            default: return null;
        }
    }
   
}

