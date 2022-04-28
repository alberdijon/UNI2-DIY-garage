/*
 * This software has been developed by Uni2
 * Under the GNU General Public License
 */
package model;

import java.util.ArrayList;
import javax.swing.table.AbstractTableModel;

/**
 *
 * @author rodriguez.markel
 */
public class ProductSoldTable extends AbstractTableModel{
    private ArrayList<ProductSold> product = new ArrayList<>();
    private final String[] columnName = {"Client-DNI, Product-ID, Amount, Date, Hour, Total_price"};

     public ProductSoldTable(ArrayList<ProductSold> product){
        this.product = product;
     
    }
     
    @Override
    public int getRowCount() {
        return product.size();
    }

    @Override
    public int getColumnCount() {
        return columnName.length;
    }
   
    @Override
    public String getColumnName(int column){
        return columnName[column];
    }
   
    @Override
    public Object getValueAt(int rowIndex, int columnIndex) {
       switch(columnIndex){
            case 0: return product.get(rowIndex).getClientDni();
            case 1: return product.get(rowIndex).getProductId();
            case 2: return product.get(rowIndex).getAmount();
            case 3: return product.get(rowIndex).getDate();
            case 4: return product.get(rowIndex).getHour();
            case 5: return product.get(rowIndex).getTotalPrice();
            default: return null;
        }
    }
   
}

