/*
 * This software has been developed by Uni2
 * Under the GNU General Public License
 */
package model;

import java.util.ArrayList;
import javax.swing.table.AbstractTableModel;

/**
 *
 * @author agirrezabala.peru
 */
public class PopularItemsTable extends AbstractTableModel {
    private ArrayList<PopularItems> pitems = new ArrayList<>();
    private final String[] columnName = {"ID", "Name", "Brand", "Stock"};
    
    public PopularItemsTable(ArrayList<PopularItems> popular){
        this.pitems=popular;
    }
    
    @Override
    public int getRowCount() {
        return pitems.size();
    }
    public int getColumnCount(){
        return columnName.length;
    }
    @Override
    public String getColumnName(int column){
        return columnName[column];
    }
    public Object getValueAt(int rowIndex, int columnIndex) {
        
        switch(columnIndex){
            
            case 0: return pitems.get(rowIndex).getId();
            case 1: return pitems.get(rowIndex).getName();
            case 2: return pitems.get(rowIndex).getBrand();
            case 3: return pitems.get(rowIndex).getStock();

            default: return null;
        }
    }
}
